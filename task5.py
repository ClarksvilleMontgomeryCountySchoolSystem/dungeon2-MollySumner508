good = r"""
                                     ,
             )
        (        /(
         \yYYy,_I_`;
         JgLFO^JL_
         \ `-  \, ` Qr+as
          `
"""
bad = r"""
                  _..
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//  fsc

"""
escaped = True
if escaped:
    outcome = "Legend: Huzzah I've escaped form my tourture!"
    print(good)
else:
    outcome = "Doom: Back to the dungeon I go..."
    print(bad)
print(outcome)