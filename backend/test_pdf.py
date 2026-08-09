from backend.ml.pdf_parser import extract_text_from_pdf


pdf_path = "backend/test_data/resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("\n========== EXTRACTED RESUME TEXT ==========\n")
print(text)

print("\n============================================")
print(f"Characters extracted: {len(text)}")