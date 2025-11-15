import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("[ERROR] Pillow (PIL) não está instalado. Execute: pip install pillow")
    sys.exit(1)


def main():
    # Diretórios padrão
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "dashboards" / "Performance-Comercial" / "images"
    out_dir = repo_root / "assets" / "screenshots"

    out_dir.mkdir(parents=True, exist_ok=True)

    # Seleciona as duas primeiras imagens page-*.png em ordem
    pngs = sorted(src_dir.glob("page-*.png"))
    if len(pngs) < 2:
        print(f"[ERROR] Menos de 2 imagens encontradas em {src_dir}")
        sys.exit(2)

    mapping = [(pngs[0], out_dir / "pg01.jpg"), (pngs[1], out_dir / "pg02.jpg")]

    for src, dst in mapping:
        img = Image.open(src).convert("RGB")
        img.save(dst, format="JPEG", quality=90)
        print(f"[OK] {src.name} -> {dst.relative_to(repo_root)}")

    print("[DONE] Conversão concluída. Imagens disponíveis em assets/screenshots/pg01.jpg e pg02.jpg")


if __name__ == "__main__":
    main()