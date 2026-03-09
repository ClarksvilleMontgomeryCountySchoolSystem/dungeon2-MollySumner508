good = r"""
       .^----^.
      (= o  O =)
       (___V__)
cf      _|==|_
   ___/' |--| |
  / ,._| |  | '
 | \__ |__}-|__}
  \___)`

"""
bad = r"""
                                        #
                                    #
                                    #
                          ^..^ #####
                          =TT=      ;
                           #########
                           # #   # #    lmg
                           M M   M M
"""
has_key = True
if not has_key:
    outcome = "Doom: Find another key"
    print(bad)
else:
    outcome = "Click: You may move forward"
    print(good)
print(outcome)