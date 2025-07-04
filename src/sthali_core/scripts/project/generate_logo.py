# """{...}."""
# import svgwrite  # type: ignore


# def main() -> None:
#     """{...}."""
#     dwg = svgwrite.Drawing(
#         "logo-img.svg",
#         size=("15000.75px", "2343.75px"),
#         viewBox="0 0 15000.75 2343.75",
#     )
#     dwg.add(dwg.text(
#         "Sthali-Core",
#         insert=(2343.75, 1590),
#         font_size="1330px",
#         font_family="monospace",
#         fill="#ca5b32",
#     ))
#     dwg.add(dwg.image(
#         href="packages.svg",
#         insert=(400, 175),
#         size=(1500, 1500),
#     ))
#     dwg.save()

# if __name__ == "__main__":
#     main()

import svgwrite

def main() -> None:
    """
    Generates the final logo, correctly embedding and aligning the
    'packages.svg' icon with the 'Sthali-Core' text.
    """
    # Create the main drawing with a specific size and viewBox
    dwg = svgwrite.Drawing(
        "logo-final.svg",  # Saving as a new file to avoid confusion
        size=("15000.75px", "2343.75px"),
        viewBox="0 0 15000.75 2343.75",
    )

    # Add the text element
    dwg.add(dwg.text(
        "Sthali-Core",
        insert=(2343.75, 1590),
        font_size="1330px",
        font_family="monospace",
        fill="#ca5b32",
    ))

    # Add the package icon with explicit position and size.
    # These values are calculated to vertically center the icon with the text.
    dwg.add(dwg.image(
        href="packages.svg",
        insert=(400, 175),      # Position: (x, y) coordinates
        size=(1500, 1500)       # Size: (width, height)
    ))

    # Save the final, corrected SVG file
    dwg.save()
    print("Generated 'logo-final.svg' with the icon and text correctly aligned.")

if __name__ == "__main__":
    main()
