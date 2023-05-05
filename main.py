def xor_pyramid(bottom_row):
current_row = bottom_row
   while len(current_row) > 1:
 next_row = [current_row[i] ^ current_row[i + 1] for i in range(len(current_row) - 1)]
 next_row.append(current_row[-1])
 current_row = next_row
return current_row[0]
for i in range(n):
   value = int(input(f"Introduceti valoarea {i + 1}: "))
bottom_row.append(value)
top_value = xor_pyramid(bottom_row)
print(f"Valoarea din varf este: {top_value}")



MOD = 666013


def count_anagrams(s, t):
   dict_t = {}
   for c in t:
      dict_t[c] = dict_t.get(c, 0) + 1

   dict_s = {}
   count = 0
   for i in range(len(s)):
      # Adaugăm caracterul curent la dicționarul dict_s
      dict_s[s[i]] = dict_s.get(s[i], 0) + 1

      # Verificăm dacă subșirul curent este anagrama șirului t
      if i >= len(t):
         # Eliminăm primul caracter din fereastră
         if dict_s[s[i - len(t)]] == 1:
            del dict_s[s[i - len(t)]]
         else:
            dict_s[s[i - len(t)]] -= 1

      if i >= len(t) - 1 and dict_s == dict_t:
         count = (count + 1) % MOD

   return count


s = input().strip()
t = input().strip()

print(count_anagrams(s, t))

if __name__ == "__main__":
   #xor_pyramid([])
   count_anagrams(s,t)