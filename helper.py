def decoreer(tekst=""): # opdracht om betreffende tekst te decoreren.
    lengte = len(tekst) + 4 # tekstlengte + 4 extra karakters.
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()