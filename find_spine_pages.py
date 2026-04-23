import pypdf

def find_spine_section(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    relevant_pages = []
    
    # Search first 50 pages for Table of Contents or keywords
    for i in range(50):
        text = reader.pages[i].extract_text()
        if "척추" in text or "추간판" in text:
            print(f"Found keyword on page {i+1}")
            
    # Search all pages for specific surgery codes
    codes = ["N1493", "N1499", "N2470", "자46"]
    for i in range(len(reader.pages)):
        text = reader.pages[i].extract_text()
        for code in codes:
            if code in text:
                print(f"Found {code} on page {i+1}")
                relevant_pages.append(i)
                break
    
    return sorted(list(set(relevant_pages)))

if __name__ == "__main__":
    pdf_path = "2026년보험심사/요양급여 책자(2026).pdf"
    pages = find_spine_section(pdf_path)
    print(f"Relevant pages: {pages}")
