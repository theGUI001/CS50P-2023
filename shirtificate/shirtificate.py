from fpdf import FPDF


class PDF:
    def __init__(self, name: str):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 50)
        self.pdf.cell(
            0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C"
        )
        self.pdf.image("shirtificate.png", w=self.pdf.epw)
        self.pdf.set_font_size(30)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self, name: str):
        self.pdf.output(name)


def main():
    name = input("Name: ").strip()
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
