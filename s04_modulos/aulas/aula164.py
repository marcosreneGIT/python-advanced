# locale para internacionalização (tradução)

# docs: 
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-
# winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar, locale


calendario_EUA = calendar.calendar(2025)

locale.setlocale(locale.LC_ALL, '') # = 'pt_BR.utf8' | localidade baseada no OS

calendario_BR = calendar.calendar(2025)

print(f'{calendario_EUA}\n'
      f'{calendario_BR }')
