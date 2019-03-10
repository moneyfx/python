n = 10
i = n - 1
j = n - 1

for row in range(n):
    for x in range(n * 2 - 1):
        if x == i or x == j or row == n - 1:
            print('*', sep='', end='')
        else:
            print(' ', sep='', end='')
    i = i - 1
    j = j + 1
    print('')
"""

         *         
        * *        
       *   *       
      *     *      
     *       *     
    *         *    
   *           *   
  *             *  
 *               * 
*******************

"""