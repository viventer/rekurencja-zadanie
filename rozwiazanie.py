def silnia(n):
    # Najpierw warunek bazowy - najprostsze rozwiązanie
    # Jeśli n jest równe 0 lub 1 nie musimy nic liczyć, 
    # wystarczy, że zwrócimy 1.
    if n == 0 or n == 1:
        return 1
    # Aby dojść do wyniku komputer musi n razy pomnożyć n, 
    # które za każdym razem będzie zmniejszane o 1.
    return n * silnia(n-1)

"""
    Przykład:
    silnia(4)
    1. Wykonanie funkcji
    return 4 * silnia(3)
    2. Wykonanie
    return 3 * silnia(2)
    3. Wykonanie
    return 2 * silnia(1)
    4. Wykonanie - spełniony warunek bazowy (n == 1)
    return 1

    Wiemy już ile, że silnia(1) = 1, więc idziemy do góry:
    2 * silnia(1) = 2 * 1 = 2 <- silnia(2)
    3 * silnia(2) = 3 * 2 = 6 <- silnia(3)
    4 * silnia(3) = 4 * 6 = 24 <- silnia(4)
    Mamy wynik - 24
"""