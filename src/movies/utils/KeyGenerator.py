# Using the Single Responsability Principle as it's only purpose is to create the preference key

class KeyGenerator:
    def original_key_generator(g1, g2, g3) -> int:
        return ((g1 * g2 * g3) % 5) + 1