class KeyGenerator:
    def original_key_generator(g1, g2, g3):
        return ((g1 * g2 * g3) % 5) + 1