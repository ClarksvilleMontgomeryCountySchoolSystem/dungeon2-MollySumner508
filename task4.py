good = r"""
                    _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        

"""
bad = r""" 
                      _' \_
                    ,' '  '`.
                   ;,)       \
                  /          :
                  (_         :
                   `--.       \
                      /        `.
                     ;           `.
                    /              `.
                   :                 `.
                   :                   \
                    \\                  \
                     ::                 :
                     || |               |
                     || |`._            ;
       Y            _;; ; __`._,       (________
   (t^##_          ((__/(_____(______,'______(___) SSt

"""
drawbridge_raised = True
if drawbridge_raised:
    outcome = "Doom: Oh nooooo"
    print(bad)
else:
    outcome = "Thunder: Crackalaka"
    print(good)
print(outcome)