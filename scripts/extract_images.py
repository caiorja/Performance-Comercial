"""
Extrai imagens das páginas do PDF (exceto a capa) e salva em dashboards/Performance-Comercial/images

Requisitos: PyMuPDF (fitz)
"""

from pathlib import Path
import sys

try:
    import fitz  # PyMuPDF
except Exception as e:
    print("PyMuPDF (fitz) não está instalado. Erro:", e)
    sys.exit(1)


def extract_images_from_pdf(pdf_path: Path, output_dir: Path, zoom: float = 2.0, skip_first_page: bool = True) -> int:
    """Renderiza páginas do PDF como PNG e salva no diretório informado.

    Args:
        pdf_path: Caminho do arquivo PDF.
        output_dir: Diretório de saída onde as imagens serão salvas.
        zoom: Fator de zoom para aumentar a resolução das imagens.
        skip_first_page: Se True, ignora a primeira página (capa).

    Returns:
        Quantidade de imagens geradas.
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF não encontrado: {pdf_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    start_index = 1 if skip_first_page else 0

    images_count = 0
    mat = fitz.Matrix(zoom, zoom)
    for i in range(start_index, total_pages):
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        # nome do arquivo: page-<num_pagina+1>.png (mantém numeração original do PDF)
        out_name = output_dir / f"page-{i+1:02d}.png"
        pix.save(out_name)
        images_count += 1
    doc.close()
    return images_count


def main():
    base_dir = Path(__file__).resolve().parent.parent  # pasta "Performance Comercial"
    pdf_path = base_dir / "Performance Comercial.pdf"
    output_dir = base_dir / "dashboards" / "Performance-Comercial" / "images"

    try:
        count = extract_images_from_pdf(pdf_path, output_dir, zoom=2.0, skip_first_page=True)
        print(f"Extração concluída. {count} imagens salvas em: {output_dir}")
    except Exception as e:
        print("Falha ao extrair imagens:", e)
        sys.exit(2)


if __name__ == "__main__":
    main()
