# This is what you would get if you buy Cookie Clicker off of Temu
# Cookie Clicker is free btw so I don't know why you would spend money for it

from raylib import *
import time

COOKIE_X = 170
COOKIE_Y = 280
COOKIE_HITBOX_RADIUS = 134

UPGRADE_FONT_SIZE = 25

upgrades = {
    "cursor": {
        "name": "Cursor",
        "cost": 10,
        "cps": 0.2,
        "owned": 0,
        "pos": (750, 50),
        "scale": 0.5,
    },
    "grandma": {
        "name": "Grandma",
        "cost": 50,
        "cps": 2,
        "owned": 0,
        "pos": (760, 340),
        "scale": 0.3,
    },
    "farm": {
        "name": "Farm",
        "cost": 500,
        "cps": 12,
        "owned": 0,
        "pos": (760, 575),
        "scale": 0.38,
    },
    "mine": {
        "name": "Mine",
        "cost": 2400,
        "cps": 60,
        "owned": 0,
        "pos": (970, 60),
        "scale": 0.3,
    },
    "factory": {
        "name": "Factory",
        "cost": 10000,
        "cps": 360,
        "owned": 0,
        "pos": (980, 330),
        "scale": 0.3,
    },
}


def mouse_over_cookie() -> bool:
    mouse = GetMousePosition()

    dx = mouse.x - COOKIE_X
    dy = mouse.y - COOKIE_Y

    return dx * dx + dy * dy <= COOKIE_HITBOX_RADIUS * COOKIE_HITBOX_RADIUS


def main() -> None:
    InitWindow(1200, 900, b"Cookie Clicker (from Temu)")
    SetTargetFPS(60)

    textures = {
        "cookie": LoadTexture(b"assets/cookie.png"),
        "cursor": LoadTexture(b"assets/cursor.png"),
        "grandma": LoadTexture(b"assets/grandma.png"),
        "farm": LoadTexture(b"assets/farm.png"),
        "mine": LoadTexture(b"assets/mine.png"),
        "factory": LoadTexture(b"assets/factory.png"),
    }

    cookies = 0.0
    cookie_held = False

    last_time = time.time()

    while not WindowShouldClose():

        # ================= TIME + CPS =================

        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        cps = 0.0
        for upgrade in upgrades.values():
            cps += upgrade["cps"] * upgrade["owned"]

        cookies += cps * dt

        # ================= CLICK COOKIE =================

        if IsMouseButtonPressed(MOUSE_BUTTON_LEFT) and mouse_over_cookie():
            cookie_held = True

        if cookie_held and IsMouseButtonReleased(MOUSE_BUTTON_LEFT):
            cookies += 1
            cookie_held = False

        # ================= BUY UPGRADES =================

        if IsMouseButtonPressed(MOUSE_BUTTON_LEFT):
            mouse = GetMousePosition()

            for key, upgrade in upgrades.items():

                texture = textures[key]
                scale = upgrade["scale"]
                x, y = upgrade["pos"]

                rect = ffi.new(
                    "Rectangle *",
                    (
                        x,
                        y,
                        texture.width * scale,
                        texture.height * scale
                    )
                )

                if CheckCollisionPointRec(mouse, rect[0]):

                    if cookies >= upgrade["cost"]:
                        cookies -= upgrade["cost"]
                        upgrade["owned"] += 1

        # ================= DRAW =================

        BeginDrawing()
        ClearBackground((112, 125, 185, 255))

        DrawText(f"Cookies: {int(cookies)}".encode(), 40, 30, 40, WHITE)
        DrawText(f"CPS: {round(cps, 1)}".encode(), 55, 90, 28, WHITE)

        cookie_scale = 0.9 if cookie_held else 1.0
        cookie_texture = textures["cookie"]

        DrawTextureEx(
            cookie_texture,
            (
                COOKIE_X - (cookie_texture.width * cookie_scale) / 2,
                COOKIE_Y - (cookie_texture.height * cookie_scale) / 2,
            ),
            0,
            cookie_scale,
            WHITE,
        )

        for key, upgrade in upgrades.items():
            texture = textures[key]
            scale = upgrade["scale"]
            x, y = upgrade["pos"]

            DrawTextureEx(texture, (x, y), 0, scale, WHITE)

            text_y = int(y + texture.height * scale + 5)

            DrawText(upgrade["name"].encode(), x, text_y, UPGRADE_FONT_SIZE, WHITE)
            DrawText(
                f"Cost: {upgrade['cost']}".encode(),
                x,
                text_y + 30,
                UPGRADE_FONT_SIZE,
                WHITE,
            )
            DrawText(
                f"Owned: {upgrade['owned']}".encode(),
                x,
                text_y + 60,
                UPGRADE_FONT_SIZE,
                WHITE,
            )

        EndDrawing()

    CloseWindow()


if __name__ == "__main__":
    main()