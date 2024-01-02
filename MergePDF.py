#pip install PyPDF2

from PyPDF2 import PdfMerger

# By appending at the end
def by_appending():
    merger = PdfMerger()
    f1 = open("samplePdf1.pdf", "rb")
    merger.append(f1)
    merger.append("samplePdf2.pdf")
    with open("mergedPdf.pdf", "wb") as merged_file:
        merger.write(merged_file)
    f1.close()

# By inserting at a specified page no.
def by_inserting():
    merger = PdfMerger()
    merger.append("samplePdf1.pdf")
    merger.merge(0, "samplePdf2.pdf")
    with open("mergedPdf1.pdf", "wb") as merged_file:
        merger.write(merged_file)

if __name__ == "__main__":
    by_appending()
    by_inserting()
