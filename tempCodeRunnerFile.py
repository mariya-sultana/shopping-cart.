 # arg1 = int(request.args['arg1'])
        # if (arg1 != 0):
        #     cartItem = db.execute("SELECT quantity FROM cart \
        #                    WHERE user_id = :id AND p_id=:symbol",
        #                           id=session["user_id"], symbol=arg1)
        #     if not cartItem:
        #         db.execute("INSERT INTO cart (quantity, pid, user_id) VALUES (1 ,:pid, :user_id)",
        #                    pid=arg1, user_id=session["user_id"])
        #         flash("item added to cart")
        #     else:
        #         cartItem[0]["quantity"] = cartItem[0]["quantity"] + 1
        #         db.execute("update cart set quantity=:quantity where p_id= :p_id and user_id = :id",
        #                    quantity=cartItem[0]["quantity"], pid=arg1, id=session["user_id"])
        #         flas