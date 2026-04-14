# 将训练用 caption 压缩为风格友好短句（一次性/可复跑）
from pathlib import Path

CAP_DIR = Path(
    r"F:\Cursor_project\ComfyUI_Project\lora_model\data\train\captions"
)

# 与 jpfantasy_style_0001 ~ 0028 一一对应；保留触发词，弱化营销长句与重复技法堆砌
COMPRESSED: dict[int, str] = {
    1: "jpfantasy_style, train dining car attendant, clouds outside the windows, warm lamplight on wood and brass, cozy fantasy travel mood, anime lineart, soft cel shading",
    2: "jpfantasy_style, idol on arena stage, lasers and confetti, glossy costume, sharp lineart, concert key visual, polished cel shading",
    3: "jpfantasy_style, guild kitchen chef, chaotic pots and steam, warm golden light, comedy expression, slice-of-life fantasy, soft cel shading",
    4: "jpfantasy_style, rookie adventurer at guild feast table, warm afternoon window light, cozy comedy mood, polished anime illustration",
    5: "jpfantasy_style, rogue in ancient ruin hall, glowing floor runes, torch versus cool magic light, dungeon exploration mood, anime cel shading",
    6: "jpfantasy_style, fox-eared apothecary at night market stall, neon lanterns and glass bottles, vivid color contrast, glossy highlights",
    7: "jpfantasy_style, healer in church chapel, stained-glass colored light on marble, serene mood, restrained elegant palette, soft anime shading",
    8: "jpfantasy_style, shrine maiden on festival stone steps, lanterns and torii, golden bokeh, cherry petals with snow, slice-of-life fantasy atmosphere",
    9: "jpfantasy_style, astrologer in observatory dome, constellation dress, cosmic glow and indigo palette, elegant anime lighting",
    10: "jpfantasy_style, forest ranger riding white stag, sun-dappled woodland ruins, adventure fantasy mood, clean lineart, cinematic light",
    11: "jpfantasy_style, elf archer in bioluminescent crystal cavern, cool rim light on face, wide heroic composition, fantasy quest mood",
    12: "jpfantasy_style, diver in submerged hall, stained-glass mermaid murals, turquoise god rays and bubbles, wonder mood, polished anime splash",
    13: "jpfantasy_style, fisher girl on sunny wooden pier, sparkling sea, cheerful expression, slice-of-life coastal fantasy, soft gradients",
    14: "jpfantasy_style, beach summer event girl, straw hat and swimsuit, bright sun on skin and water, festive background blur, anime key visual",
    15: "jpfantasy_style, volcano researcher at crater railing, lava glow and heat shimmer, sci-fantasy expedition mood, dramatic warm-cool contrast",
    16: "jpfantasy_style, noble teatime on palace terrace, sunset soft light, roses and distant towers, romantic pastel palette, painterly anime background",
    17: "jpfantasy_style, beast-eared shopkeeper at festival plaza, stalls and lanterns, candy colors, outdoor event banner composition",
    18: "jpfantasy_style, sword trainee boy in arena locker corridor, sweat and determination, tournament arc mood, sporty anime shading",
    19: "jpfantasy_style, caravan guard with flower-field wagon road, spring sunlight and petals, gentle adventure comedy, cel shading",
    20: "jpfantasy_style, steampunk mechanic girl in workshop, sparks and warm metal light, brass automaton, rich material textures, three-quarter view",
    21: "jpfantasy_style, shrine maiden purification at misty swamp altar, talismans and violet fog, eerie green reflections, dark-cute fantasy anime",
    22: "jpfantasy_style, idol in surreal candlelit mirror hallway, pink-purple glow, nervous comedy mood, strong perspective, refined shading",
    23: "jpfantasy_style, novice mage in stormy gothic library, lightning through stained glass, floating runes, cinematic key visual, cel shading",
    24: "jpfantasy_style, paladin on frozen cliff under aurora, moonlit blue palette, windblown cape and snow, heroic fantasy key art",
    25: "jpfantasy_style, onsen inn corridor with lanterns and steam, winter window snow, cozy embarrassed mood, slice-of-life fantasy illustration",
    26: "jpfantasy_style, harbor clerk at foggy pier booth, cold teal ambient with warm lantern pools, coastal slice-of-life fantasy",
    27: "jpfantasy_style, sleepy mage student in classroom at dusk, candle and tall windows, academy slice-of-life mood, clean readable props",
    28: "jpfantasy_style, beast-tamer feeding tiny dragon in golden rice fields at sunset, peaceful smile, warm rim light, rural cozy fantasy",
}


def main() -> None:
    for i, text in COMPRESSED.items():
        path = CAP_DIR / f"jpfantasy_style_{i:04d}.txt"
        if not path.exists():
            raise SystemExit(f"missing {path.name}")
        path.write_text(text.strip() + "\n", encoding="utf-8")
    print("updated", len(COMPRESSED), "captions")


if __name__ == "__main__":
    main()
