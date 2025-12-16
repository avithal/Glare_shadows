import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_soft_shadow(img, shadow_strength=0.5):
    h, w = img.shape[:2]

    # Random polygon points
    top_y = np.random.randint(0, h//2)
    bot_y = np.random.randint(h//2, h)


    # Step 1: create empty mask
    mask = np.zeros((h, w), dtype=np.float32)

    # Step 2: random shadow polygon
    poly = np.array([[
        (np.random.randint(0, w//2), top_y),
        (np.random.randint(w//2, w), top_y++ np.random.randint(40,120)),
        (w, bot_y),
        (0, bot_y-+ np.random.randint(40,120))
    ]], dtype=np.int32)

    cv2.fillPoly(mask, poly, 1.0)

    # Step 3: blur mask edges (CRITICAL)
    blur_size = np.random.randint(51, 151) | 1  # must be odd
    mask = cv2.GaussianBlur(mask, (blur_size, blur_size), 0)

    # Step 4: scale shadow intensity
    mask = mask * shadow_strength

    # Step 5: apply alpha blending
    shadowed = img.astype(np.float32)
    for c in range(3):
        shadowed[:, :, c] *= (1 - mask)

    return shadowed.astype(np.uint8)


def add_sun_glare(img, intensity=0.8):
    h, w = img.shape[:2]

    # Random sun position
    cx = np.random.randint(0, w)
    cy = np.random.randint(0, h // 2)

    # Create flare overlay
    overlay = img.copy()
    radius = np.random.randint(100, 300)
    val_glare = np.random.randint(210, 255)

    for r in range(1, radius, 4):
        alpha = intensity * (1 - r / radius)
        cv2.circle(overlay, (cx, cy), r, (val_glare, val_glare, val_glare), -1)
        img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    return img


def add_random_shadow(img):
    h, w = img.shape[:2]

    # Random polygon points
    top_y = np.random.randint(0, h//2)
    bot_y = np.random.randint(h//2, h)

    shadow_poly = np.array([[
        [0, top_y],
        [w, top_y + np.random.randint(40,120)],
        [w, bot_y],
        [0, bot_y - np.random.randint(40,120)]
    ]])

    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(mask, shadow_poly, 255)

    # Shadow intensity
    alpha = np.random.uniform(0.4, 0.6)

    # Apply darkening
    shadow = img.copy()
    shadow[mask == 255] = (shadow[mask == 255] * alpha).astype(np.uint8)
    return shadow


if __name__ == "__main__":
    # read image
    roof_image_orig = cv2.imread('original.png')
    sun_glare = add_sun_glare(roof_image_orig)
    shadow_image = add_soft_shadow(roof_image_orig)

    # Create figure
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(roof_image_orig)
    plt.title("Roof _image 1")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(sun_glare)
    plt.title("sun_glare")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(shadow_image)
    plt.title("shadow_image")
    plt.axis("off")

    plt.show()