# 从 USO 参考图工程导入训练图与 caption（一次性脚本）
import os
import re
import shutil

BASE = r"F:\Cursor_project\ComfyUI_Project\USO style reference generated photo for training"
DEST_IMG = r"F:\Cursor_project\ComfyUI_Project\lora_model\data\train\images"
DEST_CAP = r"F:\Cursor_project\ComfyUI_Project\lora_model\data\train\captions"


def main() -> None:
    os.makedirs(DEST_IMG, exist_ok=True)
    os.makedirs(DEST_CAP, exist_ok=True)
    dirs = sorted(
        d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d))
    )
    if len(dirs) != 28:
        raise SystemExit(f"预期 28 个子文件夹，实际 {len(dirs)}")

    for i, folder in enumerate(dirs, 1):
        fp = os.path.join(BASE, folder)
        files = [
            f
            for f in os.listdir(fp)
            if os.path.isfile(os.path.join(fp, f))
            and f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]
        files = [f for f in files if "雪菲" not in f]
        train = None
        for f in sorted(files):
            if f.startswith("ComfyUI"):
                train = f
                break
        if not train:
            raise SystemExit(f"未找到 ComfyUI 训练图: {folder}")

        ppt = os.path.join(fp, "seed and prompt.txt")
        if not os.path.isfile(ppt):
            raise SystemExit(f"缺少 seed and prompt.txt: {folder}")

        with open(ppt, "r", encoding="utf-8") as fh:
            content = fh.read()
        m = re.search(
            r"prompt[：:]\s*\n?(.*?)(?=\n\s*seed[：:])",
            content,
            re.DOTALL | re.IGNORECASE,
        )
        if not m:
            m = re.search(r"prompt[：:]\s*(.+)", content, re.DOTALL | re.IGNORECASE)
        prompt_body = m.group(1).strip() if m else content.strip()
        # 合并空白，保留完整词句
        prompt_body = " ".join(prompt_body.split())
        cap = prompt_body
        if "jpfantasy_style" not in cap.lower():
            cap = "jpfantasy_style, " + cap

        ext = os.path.splitext(train)[1].lower() or ".png"
        new_base = f"jpfantasy_style_{i:04d}"
        new_img = new_base + ext
        shutil.copy2(os.path.join(fp, train), os.path.join(DEST_IMG, new_img))
        with open(
            os.path.join(DEST_CAP, new_base + ".txt"),
            "w",
            encoding="utf-8",
            newline="\n",
        ) as out:
            out.write(cap)
        print(i, folder, "->", new_img)

    print("完成:", len(dirs), "对")


if __name__ == "__main__":
    main()
