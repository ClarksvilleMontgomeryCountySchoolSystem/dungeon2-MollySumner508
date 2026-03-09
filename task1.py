good = r"""
             
                              / )
              (\__/)         ( (
              )    (          ) )
            ={      }=       / /
              )     `-------/ /
             (               /
              \              |
             ,'\       ,    ,'
             `-'\  ,---\   | \
                _) )    `. \ /
               (__/       ) )   hjw
                         (_/
"""
bad = r"""
                   ,
                 \)\_
                /    '. .---._
              =P ^     `      '.
               `--.       /     \
               .-'(       \      |
              (.-'   )-..__>   , ;
              (_.--``    (__.-/ /
                      .-.__.-'.'
                jgs    '-...-'
"""


torch_lit = True
if torch_lit:
    outcome = "Flicker: You have light"
    print(good)
else:
    outcome = "Doom: Try again"
    print(bad)
print(outcome)