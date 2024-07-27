# 9 - Palindrome Number

# Given an integer x, return true if x is a 
# palindrome, and false otherwise. (An integer 
# is a palindrome when it reads the same 
# backward as forward. For example, 121 is 
# palindrome while 123 is not.)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Se o x for um número negativo, ele 
        # não é um palíndromo, então vou 
        # verificar isso
        if x < 0:
            return False

        # Agora vamos converter o número em uma 
        # string e em seguida verificar se ele 
        # invertido é igual ao original
        x = str(x)

        # o -1 é para inverter a string :)
        return x == x[::-1]
    
# Sobre a eficiência do código, ele é 
# intermediário, usando 32 ms em runtime e 
# 11.44 MB em memória.