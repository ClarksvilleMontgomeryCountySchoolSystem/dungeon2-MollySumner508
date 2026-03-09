good = r"""
                                     ,
              ,-.       _,---._ __  / \
             /  )    .-'       `./ /   \
            (  (   ,'            `/    /|
             \  `-"             \'\   / |
              `.              ,  \ \ /  |
               /`.          ,'-`----Y   |
              (            ;        |   '
              |  ,-.    ,-'         |  /
              |  | (   |        hjw | /
              )  |  \  `.___________|/
              `--'   `--'
"""
bad = r"""
     _._     _,-'""`-._
     (,-.`._,'(       |\`-/|
         `-.-' \ )-`( , o o)
     -bf-      `-    \`_`"'-
"""
guard_awake = True
if not guard_awake:
   outcome = "Shadow: honk shoooo memememe"
   print(good)
else:
    outcome = "Doom: Find another way"
    print(bad)
print(outcome)