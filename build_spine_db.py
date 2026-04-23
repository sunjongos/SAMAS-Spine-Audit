import pypdf

def extract_specific_pages(pdf_path, pages):
    reader = pypdf.PdfReader(pdf_path)
    content = ""
    for p in pages:
        if p < len(reader.pages):
            content += f"--- Page {p+1} ---\n"
            content += reader.pages[p].extract_text() + "\n\n"
    return content

if __name__ == "__main__":
    pdf_path = "2026년보험심사/요양급여 책자(2026).pdf"
    # Earlier found pages (0-indexed for the script)
    relevant_pages = [420, 429, 434, 435, 436, 442, 470, 471, 472, 741, 742, 758, 759, 766, 767, 774, 949, 950]
    db_content = extract_specific_pages(pdf_path, relevant_pages)
    
    with open("척추심사_고시_DB.txt", "w", encoding="utf-8") as f:
        f.write(db_content)
    print("Spine Audit DB created successfully.")
