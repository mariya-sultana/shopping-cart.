from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.apps import custom_app_context as pwd_context
from helpers import apology, login_required, lookup, usd
import os
# Configure application
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///shopping.db")

# Make sure API key is set
os.environ["API_KEY"] = 'pk_90e51ad10a4b49f2a18da659384551ee'
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT * FROM trancation WHERE user_id=?", user_id)

    return render_template("history.html", transactions=transactions)

    # return render_template("history.html")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    name = db.execute(
        "select username, cash from users where id = :id ", id=session["user_id"])
    rows = db.execute("select * from cart where user_id = :id",
                      id=session["user_id"])
    invi = db.execute(
        "select * from invoice where user_id = :id", id=session["user_id"])
    count = 0
    qunt = 0
    for purchase in invi:
        count += purchase["total"]
    qnt = db.execute(
        "select * from cart where user_id = :id", id=session["user_id"])
    for purchase in qnt:
        qunt += purchase["quantity"]

    return render_template("index.html", name=name, qunt=qunt, count=count)
   


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/product", methods=["GET", "POST"])
@login_required
def product():
    """Get stock quote."""
    if request.method == "GET":
        rows = db.execute("SELECT * FROM product")

        return render_template("product.html", rows=rows)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        product = request.form.get("product")
        rows = db.execute(
            "Select * from product where name= :name", name=product)

        if not rows[0]["name"]:
            return apology("Product does not exists")

        quantity = int(request.form.get("quantity"))
        if quantity < 0:
            return apology("Enter valid quantity")
        if (quantity > rows[0]["stock"]):
            return apology("Stock not available")

        else:
            cash = db.execute(
                "Select cash from users where id=:id", id=session["user_id"])

            if not cash or float(cash[0]["cash"] < float(rows[0]["price"])):
                return apology("Not enough cash")

        db.execute("Update users set cash = cash - :bought where id = :id",
                   bought=rows[0]["price"], id=session["user_id"])
        a = rows[0]["price"]
        db.execute("INSERT INTO trancation (pname, total_BUY,total_price,total_cost,pid,user_id) VALUES(?,?,?,?,?,?)",
                   product, quantity, a, quantity * a, rows[0]["pid"], session["user_id"])

        flash('Bought')

        db.execute("insert into invoice(inv_date, total, pid, user_id) values (datetime('now', 'localtime'), :total, :p_id, :id)",
                   total=rows[0]["price"], p_id=rows[0]["pid"], id=session["user_id"])

        db.execute("Update product set stock = stock - :count where name=:name",
                   name=product, count=quantity)
        return redirect(url_for("index"))
    else:
        return render_template("buy.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must provide username", 403)

        if not password:
            return apology("must provide password", 403)

        if not confirmation or password != confirmation:
            return apology("passwords do not match", 403)

        hash = generate_password_hash(password)

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?,?)", username, hash)
            return redirect('/')
        except:
            return apology("Username already exists", 403)

    else:
        return render_template('register.html')
