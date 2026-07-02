import fitz


def load_agreement(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text() + "\n"

    doc.close()

    return text


if __name__ == "__main__":

    pdf_path = "docs/agreement.pdf"

    agreement_text = load_agreement(pdf_path)

    print("========== AGREEMENT TEXT ==========\n")

    print(agreement_text)