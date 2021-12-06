class Settings:
    screen_width = 1200
    screen_height = 720
    bg_color = (230, 230,230)

if __name__ == "__main__":
    s1 = Settings()
    s2 = Settings()

    print(s1.screen_width)
    s1.screen_width = 3000
    setattr(Settings, "screen_width", 4000)
    print(s1.screen_width)
    print(s2.screen_width)