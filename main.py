# main.py (sürükleme iyileştirilmiş tam dosya)
import os, sys, time, json, math
import pygame
from pygame.locals import *

# ---------------------------
# Initialization & Config
# ---------------------------
pygame.init()
try:
pygame.mixer.init()
except Exception:
    pass

# Window title
pygame.display.set_caption("Klo.")

SCREEN_W, SCREEN_H = 540, 900
MARGIN = 18
GRID_COLS, GRID_ROWS = 4, 5
BOARD_W = SCREEN_W - 2*MARGIN
BOARD_H = int(BOARD_W * (GRID_ROWS / GRID_COLS))
CELL_W = BOARD_W // GRID_COLS
CELL_H = BOARD_H // GRID_ROWS
FPS = 60

# Drag tuning
DRAG_THRESHOLD = 8   # px to decide axis lock
HITBOX_PADDING = 8   # px for easier selection

# Retro 8-bit/16-bit Colors & Styling (Eye-friendly version)
# Atari/NES/SNES inspired palette - Softer, less eye-straining
BG = (20, 25, 20)              # Dark gray-green background (softer than pure black)
FRAME_COLOR = (0, 180, 100)   # Softer green frame
INNER_BG = (25, 30, 22)       # Slightly lighter green tint
BOARD_BG = (30, 35, 25)       # Brighter green tint for board
GRID_LINE = (40, 80, 50)      # Darker, softer green grid lines
TEXT = (0, 200, 120)          # Softer green text (less harsh than pure neon)

# Retro 8-bit/16-bit Palette (Eye-friendly, muted but still retro)
# Colors are toned down but maintain classic game aesthetic
PALETTE = {
    "T": (220, 200, 80),       # Softer yellow - target block (golden)
    "red": (200, 80, 80),      # Muted retro red
    "magenta": (200, 120, 200), # Softer magenta/pink
    "lime": (100, 200, 100),   # Muted lime green
    "violet": (150, 100, 200), # Softer purple/violet
    "teal": (80, 200, 160),    # Muted cyan/teal
    "orange": (220, 150, 80),  # Softer orange
    "blue": (80, 120, 200),    # Muted blue
    "coral": (200, 120, 120)   # Soft pink/coral
}

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
LEVELS_DIR = os.path.join(BASE_DIR, "levels")
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(LEVELS_DIR, exist_ok=True)

# Settings
class Settings:
    def __init__(self):
        self.language = "TR"  # TR, EN
        self.sound_volume = 0.8  # 0.0 - 1.0
        self.music_volume = 0.3  # 0.0 - 1.0
        self.load()
    
    def load(self):
        try:
            if os.path.exists(SETTINGS_FILE):
                with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.language = data.get("language", "TR")
                    self.sound_volume = data.get("sound_volume", 0.8)
                    self.music_volume = data.get("music_volume", 0.3)
        except:
            pass
    
    def save(self):
        try:
            with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump({
                    "language": self.language,
                    "sound_volume": self.sound_volume,
                    "music_volume": self.music_volume
                }, f)
        except:
            pass
    
    def apply_audio(self):
        pygame.mixer.music.set_volume(self.music_volume)

settings = Settings()

# Çeviri sistemi
def get_text(key):
    translations = {
        "TR": {
            "menu_play": "Oyna",
            "menu_howto": "Nasıl Oynanır",
            "menu_settings": "Ayarlar",
            "menu_exit": "Çıkış",
            "settings_title": "Ayarlar",
            "settings_language": "Dil:",
            "settings_sound": "Ses:",
            "settings_music": "Müzik:",
            "settings_turkish": "Türkçe",
            "settings_english": "English",
            "settings_back": "Geri",
            "howto_title": "Nasıl Oynanır",
            "howto_objective": "Amaç",
            "howto_objective_text": "Hedef bloğu (2x2 sarı T bloğu) çıkışa (EXIT) taşıyın!",
            "howto_controls": "Kontroller",
            "howto_mouse": "FARE: Blokları sürükleyip bırakarak hareket ettirin",
            "howto_u": "U: Son hamleyi geri al",
            "howto_r": "R: Yeniden başla",
            "howto_esc": "ESC: Ana menüye dön",
            "howto_f11": "F11: Tam ekran modu",
            "howto_back": "Geri",
            "game_moves": "Hamle",
            "game_time": "Süre",
            "game_exit": "EXIT",
            "game_complete": "Tebrikler!",
            "game_complete_time": "Çözüm Süresi",
            "game_complete_moves": "Toplam Hamle",
            "game_restart_hint": "R tuşuyla tekrar oyna"
        },
        "EN": {
            "menu_play": "Play",
            "menu_howto": "How to Play",
            "menu_settings": "Settings",
            "menu_exit": "Exit",
            "settings_title": "Settings",
            "settings_language": "Language:",
            "settings_sound": "Sound:",
            "settings_music": "Music:",
            "settings_turkish": "Türkçe",
            "settings_english": "English",
            "settings_back": "Back",
            "howto_title": "How to Play",
            "howto_objective": "Objective",
            "howto_objective_text": "Move the target block (2x2 yellow T block) to the exit (EXIT)!",
            "howto_controls": "Controls",
            "howto_mouse": "MOUSE: Drag and drop blocks to move them",
            "howto_u": "U: Undo last move",
            "howto_r": "R: Restart",
            "howto_esc": "ESC: Return to main menu",
            "howto_f11": "F11: Fullscreen mode",
            "howto_back": "Back",
            "game_moves": "Moves",
            "game_time": "Time",
            "game_exit": "EXIT",
            "game_complete": "Congratulations!",
            "game_complete_time": "Time",
            "game_complete_moves": "Total Moves",
            "game_restart_hint": "Press R to restart"
        }
    }
    return translations.get(settings.language, translations["TR"]).get(key, key)

# 8-bit style tone generator - daha yumuşak ve retro sesler
def _make_tone(path, freq=440, dur_ms=120, vol=0.10, sr=44100, wave_type='square'):
    import wave, struct
    n = int(sr * dur_ms / 1000.0)
    with wave.open(path, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        max_amp = int(32767 * vol)
        
        for i in range(n):
            t = i / sr
            angle = 2.0 * math.pi * freq * t
            
            if wave_type == 'square':
                # 8-bit style square wave
                val = max_amp if math.sin(angle) >= 0 else -max_amp
            elif wave_type == 'triangle':
                # Yumuşak triangle wave
                val = int(max_amp * (2.0 * abs(2.0 * ((t * freq) % 1) - 1) - 1))
            else:
                # Sine wave (yumuşak)
                val = int(max_amp * math.sin(angle))
            
            wf.writeframes(struct.pack('<h', val))

# 8-bit tarzı yumuşak sesler oluştur
if not os.path.exists(os.path.join(AUDIO_DIR, "move.wav")):
    _make_tone(os.path.join(AUDIO_DIR, "move.wav"), freq=500, dur_ms=80, vol=0.25, wave_type='square')
if not os.path.exists(os.path.join(AUDIO_DIR, "click.wav")):
    _make_tone(os.path.join(AUDIO_DIR, "click.wav"), freq=350, dur_ms=60, vol=0.20, wave_type='square')
if not os.path.exists(os.path.join(AUDIO_DIR, "complete.wav")):
    # Başarı melodisi - 8-bit tarzı
    _make_tone(os.path.join(AUDIO_DIR, "complete.wav"), freq=523, dur_ms=200, vol=0.06, wave_type='square')
if not os.path.exists(os.path.join(AUDIO_DIR, "error.wav")):
    # Hata sesi - düşük frekanslı, yumuşak
    _make_tone(os.path.join(AUDIO_DIR, "error.wav"), freq=200, dur_ms=120, vol=0.06, wave_type='square')

# Müzik albümü - DavidKBD Pink Bloom Pack
MUSIC_ALBUM = [
    {"name": "Pink Bloom", "file": "DavidKBD - Pink Bloom Pack - 01 - Pink Bloom.ogg"},
    {"name": "Portal to Underworld", "file": "DavidKBD - Pink Bloom Pack - 02 - Portal to Underworld.ogg"},
    {"name": "To the Unknown", "file": "DavidKBD - Pink Bloom Pack - 03 - To the Unknown.ogg"},
    {"name": "Valley of Spirits", "file": "DavidKBD - Pink Bloom Pack - 04 - Valley of Spirits.ogg"},
    {"name": "Western Cyberhorse", "file": "DavidKBD - Pink Bloom Pack - 05 - Western Cyberhorse.ogg"},
    {"name": "Diamonds on The Ceiling", "file": "DavidKBD - Pink Bloom Pack - 06 - Diamonds on The Ceiling.ogg"},
    {"name": "The Hidden One", "file": "DavidKBD - Pink Bloom Pack - 07 - The Hidden One.ogg"},
    {"name": "Lost Spaceship's Signal", "file": "DavidKBD - Pink Bloom Pack - 08 - Lost Spaceship's Signal.ogg"},
    {"name": "Lightyear City", "file": "DavidKBD - Pink Bloom Pack - 09 - Lightyear City.ogg"},
]

def safe_load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except Exception:
        return None

SND_MOVE = safe_load_sound(os.path.join(AUDIO_DIR, "move.wav"))
SND_COMPLETE = safe_load_sound(os.path.join(AUDIO_DIR, "complete.wav"))
SND_ERROR = safe_load_sound(os.path.join(AUDIO_DIR, "error.wav"))
SND_CLICK = safe_load_sound(os.path.join(AUDIO_DIR, "click.wav"))

# Ses efektleri için volume wrapper
def play_sound(snd):
    if snd:
        snd.set_volume(settings.sound_volume)
        snd.play()

# ---------------------------
# Pygame screen & fonts
# ---------------------------
window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen = pygame.Surface((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

# Mouse koordinatlarını fullscreen'e göre dönüştür
def transform_mouse_pos(pos):
    """Fullscreen modda mouse koordinatlarını oyun canvas'ına çevirir"""
    if 'game' in globals() and getattr(game, 'fullscreen', False):
        display_surface = pygame.display.get_surface()
        info = pygame.display.Info()
        display_w, display_h = info.current_w, info.current_h
        # Ekrana sığdırma ölçeği (letterbox)
        scale = min(display_w / SCREEN_W, display_h / SCREEN_H)
        scaled_w = max(1, int(SCREEN_W * scale))
        scaled_h = max(1, int(SCREEN_H * scale))
        offset_x = (display_w - scaled_w) // 2
        offset_y = (display_h - scaled_h) // 2
        # Ters dönüşüm: ekran koordinatları → canvas koordinatları
        mx, my = pos
        # Offset'i çıkar ve scale'a böl
        transformed_x = int((mx - offset_x) / scale)
        transformed_y = int((my - offset_y) / scale)
        return transformed_x, transformed_y
    else:
        return pos

# Tam ekran sunumu için ölçekleyip ortalayan yardımcı
def present():
    if 'game' in globals() and getattr(game, 'fullscreen', False):
        display_surface = pygame.display.get_surface()
        info = pygame.display.Info()
        display_w, display_h = info.current_w, info.current_h
        # Ekrana sığdırma ölçeği (letterbox)
        scale = min(display_w / SCREEN_W, display_h / SCREEN_H)
        scaled_w = max(1, int(SCREEN_W * scale))
        scaled_h = max(1, int(SCREEN_H * scale))
        offset_x = (display_w - scaled_w) // 2
        offset_y = (display_h - scaled_h) // 2
        display_surface.fill((0, 0, 0))
        scaled = pygame.transform.smoothscale(screen, (scaled_w, scaled_h))
        display_surface.blit(scaled, (offset_x, offset_y))
        pygame.display.flip()
    else:
        # Pencere modunda doğrudan aktar
        window.blit(screen, (0, 0))
        pygame.display.flip()

# Window icon ekle
try:
    icon = pygame.image.load(os.path.join(BASE_DIR, "logo.png"))
    pygame.display.set_icon(icon)
except:
    pass

# Font'ları yükle (Bytesized pixel font)
FONTS_DIR = os.path.join(BASE_DIR, "assets", "fonts")
os.makedirs(FONTS_DIR, exist_ok=True)

# Bytesized font yolu
bytesized_font_path = os.path.join(FONTS_DIR, "Bytesized.ttf")

# Font yükle
try:
    if os.path.exists(bytesized_font_path):
        font = pygame.font.Font(bytesized_font_path, 18)
        bigfont = pygame.font.Font(bytesized_font_path, 28)
        titlefont = pygame.font.Font(bytesized_font_path, 32)
    else:
        # Font yoksa bold efekt için manuel render
        font = pygame.font.SysFont("Consolas", 18)
        bigfont = pygame.font.SysFont("Consolas", 28)
        titlefont = pygame.font.SysFont("Consolas", 32)
except Exception as e:
    # Fallback font'lar
    font = pygame.font.Font(None, 18)
    bigfont = pygame.font.Font(None, 28)
    titlefont = pygame.font.Font(None, 32)

def draw_text(surf, text, pos, f=font, color=TEXT):
    surf.blit(f.render(text, True, color), pos)

# ---------------------------
# Levels
# ---------------------------
def load_level(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ensure_sample_levels():
    # if levels folder empty, create two sample levels (safe fallback)
    try:
        files = [fn for fn in os.listdir(LEVELS_DIR) if fn.endswith(".json")]
    except FileNotFoundError:
        files = []
    if not files:
        sample_a = {
            "id":"A-01",
            "grid":{"cols":4,"rows":5},
            "blocks":[
                {"id":"T","w":2,"h":2,"x":1,"y":0,"type":"target","color":"T"},
                {"id":"L","w":1,"h":2,"x":0,"y":0,"color":"red"},
                {"id":"R","w":1,"h":2,"x":3,"y":0,"color":"violet"},
                {"id":"B1","w":1,"h":2,"x":0,"y":2,"color":"teal"},
                {"id":"B2","w":1,"h":2,"x":3,"y":2,"color":"blue"},
                {"id":"M","w":2,"h":1,"x":1,"y":2,"color":"orange"},
                {"id":"s1","w":1,"h":1,"x":1,"y":3,"color":"magenta"},
                {"id":"s2","w":1,"h":1,"x":2,"y":3,"color":"lime"}
            ],
            "par":20,
            "exit":[1,3],
            "difficulty":2
        }
        sample_b = {
            "id":"B-01",
            "grid":{"cols":4,"rows":5},
            "blocks":[
                {"id":"T","w":2,"h":2,"x":1,"y":0,"type":"target","color":"T"},
                {"id":"a","w":1,"h":1,"x":0,"y":1,"color":"coral"},
                {"id":"b","w":1,"h":1,"x":3,"y":1,"color":"magenta"},
                {"id":"c","w":2,"h":1,"x":1,"y":2,"color":"orange"},
                {"id":"d","w":1,"h":2,"x":0,"y":2,"color":"teal"},
                {"id":"e","w":1,"h":2,"x":3,"y":2,"color":"blue"}
            ],
            "par":28,
            "exit":[1,3],
            "difficulty":4
        }
        os.makedirs(LEVELS_DIR, exist_ok=True)
        with open(os.path.join(LEVELS_DIR, "A-01.json"), "w", encoding="utf-8") as f:
            json.dump(sample_a, f, ensure_ascii=False, indent=2)
        with open(os.path.join(LEVELS_DIR, "B-01.json"), "w", encoding="utf-8") as f:
            json.dump(sample_b, f, ensure_ascii=False, indent=2)

def list_levels():
    ensure_sample_levels()
    ret = []
    for fn in sorted(os.listdir(LEVELS_DIR)):
        if fn.endswith(".json"):
            data = load_level(os.path.join(LEVELS_DIR, fn))
            ret.append((data.get("id", fn[:-5]), fn))
    return ret

# ---------------------------
# Core classes
# ---------------------------
class Block:
    def __init__(self, bid, w, h, x, y, color_name="T", is_target=False):
        self.id = bid
        self.w = w; self.h = h
        self.x = x; self.y = y
        self.is_target = is_target
        self.color = PALETTE.get(color_name, PALETTE["T"])
        self.rect = pygame.Rect(MARGIN + x*CELL_W, MARGIN + 120 + y*CELL_H, w*CELL_W, h*CELL_H)
        self.pixel_target = (self.rect.x, self.rect.y)
        # drag/runtime state
        self.drag_start_px = None
        self.axis_locked = None
        self.offset = (0,0)

    def update_rect(self):
        self.rect.x = MARGIN + self.x * CELL_W
        self.rect.y = MARGIN + 120 + self.y * CELL_H
        self.rect.w = self.w * CELL_W
        self.rect.h = self.h * CELL_H
        self.pixel_target = (self.rect.x, self.rect.y)

    def draw(self, surf, dragging=False, preview=False):
        # Retro block drawing with eye-friendly muted colors
        # Apply subtle darkening for less eye strain while maintaining retro look
        base_color = self.color
        # Slightly darken colors for better viewing comfort
        muted_color = (max(0, base_color[0] - 15), max(0, base_color[1] - 15), max(0, base_color[2] - 15))
        
        pygame.draw.rect(surf, muted_color, self.rect, border_radius=6)
        
        # Softer retro border - less bright, more subtle
        if self.is_target:
            border_color = (200, 180, 100)  # Softer golden yellow
        else:
            # Increase brightness slightly for border but keep it muted
            border_brighter = (min(255, muted_color[0] + 40), min(255, muted_color[1] + 40), min(255, muted_color[2] + 40))
            border_color = border_brighter
        
        pygame.draw.rect(surf, border_color, self.rect, width=2, border_radius=6)
        
        if preview:
            # Very subtle glow for preview
            pygame.draw.rect(surf, (0, 140, 80), self.rect, width=2, border_radius=6)
        
        if dragging:
            # Subtle glow when dragging
            for i in range(2):
                glow_rect = pygame.Rect(self.rect.x - i, self.rect.y - i, self.rect.w + 2*i, self.rect.h + 2*i)
                glow_alpha = max(0, 60 - i*30)
                glow_surf = pygame.Surface((glow_rect.w, glow_rect.h), pygame.SRCALPHA)
                # Use border color with alpha for subtle glow
                if len(border_color) >= 3:
                    glow_color_rgba = (*border_color[:3], glow_alpha)
                else:
                    glow_color_rgba = (*border_color, glow_alpha)
                pygame.draw.rect(glow_surf, glow_color_rgba, (0, 0, glow_rect.w, glow_rect.h), border_radius=6 + i)
                surf.blit(glow_surf, glow_rect.topleft)
            pygame.draw.rect(surf, border_color, self.rect, width=2, border_radius=6)
        
        # Text with good contrast - all blocks use light text for consistency
        # Only use dark text for very bright blocks (threshold increased)
        avg_brightness = sum(muted_color)/3
        if avg_brightness > 190:  # Only very bright blocks get dark text
            text_color = (20, 20, 20)  # Very dark gray instead of pure black
        else:
            text_color = (240, 240, 240)  # Light text for all other blocks (consistent with others)
        
        # Subtle shadow for retro effect - always use dark shadow for readability
        shadow_surf = font.render(self.id, True, (20, 20, 20))
        surf.blit(shadow_surf, (self.rect.x+9, self.rect.y+9))
        draw_text(surf, self.id, (self.rect.x+8, self.rect.y+8), font, color=text_color)

    def animate_towards_pixel_target(self, speed=1200, dt=1/60.0):
        """Çok daha hızlı ve akıcı animasyon"""
        tx, ty = self.pixel_target
        dx = tx - self.rect.x
        dy = ty - self.rect.y
        dist = math.hypot(dx, dy)
        
        # Çok yakın ise direkt ata
        if dist < 0.5:
            self.rect.x, self.rect.y = tx, ty
            return True
        
        # Smooth ease-out cubic interpolation
        if dist > 50:
            # Uzak mesafe: tam hız
            t = 1.0
        elif dist > 10:
            # Orta mesafe: quadratic yavaşla
            t = dist / 50.0
            t = t * t  # Quadratic ease-out
        else:
            # Çok yakın: ease-out cubic
            t = dist / 10.0
            t = t * t * (3 - 2 * t)  # Smoothstep
        
        # Hızı hesapla - daha hızlı ve responsive
        step = speed * dt * t
        step = min(step, dist)
        
        # Hareket et
        if dist > 0.5:
            self.rect.x += dx / dist * step
            self.rect.y += dy / dist * step
        
        return False

class Board:
    def __init__(self, cols, rows, blocks_def, exit_pos):
        self.cols = cols; self.rows = rows
        self.blocks = {}
        for b in blocks_def:
            color = b.get("color")
            self.blocks[b["id"]] = Block(b["id"], b["w"], b["h"], b["x"], b["y"], color_name=color, is_target=(b.get("type")=="target"))
        self.exit = tuple(exit_pos)
        self.history = []

    def occupancy(self, ignore=None):
        grid = [[None for _ in range(self.cols)] for __ in range(self.rows)]
        for bid, blk in self.blocks.items():
            if bid == ignore: continue
            for yy in range(blk.y, blk.y + blk.h):
                for xx in range(blk.x, blk.x + blk.w):
                    grid[yy][xx] = bid
        return grid

    def can_move(self, bid, dx, dy):
        blk = self.blocks[bid]
        nx, ny = blk.x + dx, blk.y + dy
        if nx < 0 or ny < 0 or nx + blk.w > self.cols or ny + blk.h > self.rows:
            return False
        occ = self.occupancy(ignore=bid)
        for yy in range(ny, ny + blk.h):
            for xx in range(nx, nx + blk.w):
                if occ[yy][xx] is not None:
                    return False
        return True

    def slide_one(self, bid, dx, dy, record=True):
        if record:
            self.save()
        if self.can_move(bid, dx, dy):
            blk = self.blocks[bid]
            blk.x += dx; blk.y += dy
            blk.update_rect()
            blk.pixel_target = (blk.rect.x, blk.rect.y)
            return True
        if record and self.history:
            self.history.pop()
        return False

    def save(self):
        self.history.append({k:(v.x, v.y) for k,v in self.blocks.items()})
        if len(self.history) > 400: self.history.pop(0)

    def undo(self):
        if not self.history: return
        st = self.history.pop()
        for k,(x,y) in st.items():
            b = self.blocks[k]
            b.x, b.y = x, y
            b.update_rect()
            b.pixel_target = (b.rect.x, b.rect.y)

    def is_solved(self):
        for b in self.blocks.values():
            if b.is_target:
                return (b.x, b.y) == self.exit
        return False

# ---------------------------
# Solver (BFS)
# ---------------------------

# ---------------------------
# Game & UI
# ---------------------------
class Game:
    def __init__(self):
        self.levels = list_levels()
        self.current_index = 0
        self.level = None
        self.board = None
        self.moves = 0
        self.selected = None
        self.dragging = False
        self.drag_start = (0,0)
        self.preview_cell = None
        self.start_time = time.time()
        self.solved = False
        self.completion_time = 0
        self.state = "menu"  # menu, playing, settings
        self.previous_state = "menu"  # Ayarlardan geri dönmek için
        self.hovered_button = None
        self.current_music = None  # Şu anki müzik
        self.settings_slider = None  # Hangi slider'da
        self.fullscreen = False
        self.paused_duration = 0  # Toplam duraklatılan süre
        self.pause_start_time = None  # Duraklama başlangıç zamanı
        self.load_level_by_index(0)

    def load_level_by_index(self, idx):
        if not self.levels:
            ensure_sample_levels()
            self.levels = list_levels()
        self.current_index = idx % len(self.levels)
        _, fn = self.levels[self.current_index]
        self.level = load_level(os.path.join(LEVELS_DIR, fn))
        self.board = Board(self.level["grid"]["cols"], self.level["grid"]["rows"], self.level["blocks"], self.level["exit"])
        self.moves = 0
        self.selected = None
        self.dragging = False
        self.preview_cell = None
        self.start_time = time.time()
        self.solved = False
        self.paused_duration = 0
        self.pause_start_time = None
        self.initial = {k:(v.x,v.y) for k,v in self.board.blocks.items()}

    def restart(self):
        for k,(x,y) in self.initial.items():
            b = self.board.blocks[k]; b.x,b.y = x,y; b.update_rect(); b.pixel_target = (b.rect.x, b.rect.y)
        self.board.history.clear(); self.moves = 0; self.start_time = time.time(); self.solved = False; self.paused_duration = 0; self.pause_start_time = None

game = Game()

# Arkaplan müziğini başlat - Rastgele bir track seç
import random
try:
    if MUSIC_ALBUM:
        selected_track = random.choice(MUSIC_ALBUM)
        bgm_path = os.path.join(AUDIO_DIR, selected_track["file"])
        if os.path.exists(bgm_path):
            game.current_music = selected_track
            pygame.mixer.music.load(bgm_path)
            pygame.mixer.music.set_volume(settings.music_volume)
            pygame.mixer.music.play(-1)  # Sonsuz loop
except Exception as e:
    pass

# Hit testing with padding
def point_in_block_with_padding(block, px, py):
    r = block.rect.inflate(HITBOX_PADDING*2, HITBOX_PADDING*2)
    return r.collidepoint(px, py)

def pixel_to_grid_center(px, py, block):
    # Convert pixel position (top-left corner of block) to grid position
    # Account for block dimensions by offsetting from center
    gx = int((px - MARGIN) // CELL_W)
    gy = int((py - MARGIN - 120) // CELL_H)
    # For blocks larger than 1x1, adjust so preview shows at correct top-left position
    # If we get center, we need to offset by half the block size
    # But since we're using top-left position now, this should be correct
    gx = max(0, min(game.board.cols - block.w, gx))
    gy = max(0, min(game.board.rows - block.h, gy))
    return gx, gy

# ---------------------------
# Main loop
# ---------------------------
running = True
while running:
    dt = clock.tick(FPS) / 1000.0
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False

        # Ana menü state kontrolü
        if game.state == "menu":
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                mx, my = transform_mouse_pos(ev.pos)
                play_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 100, 250, 70)
                howto_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 25, 250, 70)
                settings_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 50, 250, 70)
                exit_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 125, 250, 70)
                
                if play_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    # Eğer menüden oyunu duraklatmışsak, duraklama süresini hesapla
                    if game.pause_start_time is not None:
                        # Duraklama süresini toplam duraklama süresine ekle
                        pause_duration = time.time() - game.pause_start_time
                        game.paused_duration += pause_duration
                        game.pause_start_time = None  # Duraklama bitirdi
                    game.state = "playing"
                elif howto_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    game.previous_state = "menu"
                    game.state = "howto"
                elif settings_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    game.previous_state = "menu"  # Menüden ayarlara git
                    game.state = "settings"
                elif exit_btn.collidepoint(mx, my):
                    running = False
            elif ev.type == MOUSEMOTION:
                mx, my = transform_mouse_pos(ev.pos)
                play_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 100, 250, 70)
                howto_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 25, 250, 70)
                settings_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 50, 250, 70)
                exit_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 125, 250, 70)
                if play_btn.collidepoint(mx, my):
                    game.hovered_button = "play"
                elif howto_btn.collidepoint(mx, my):
                    game.hovered_button = "howto"
                elif settings_btn.collidepoint(mx, my):
                    game.hovered_button = "settings"
                elif exit_btn.collidepoint(mx, my):
                    game.hovered_button = "exit"
                else:
                    game.hovered_button = None
            elif ev.type == KEYDOWN and ev.key == K_F11:
                # Fullscreen toggle
                game.fullscreen = not game.fullscreen
                if game.fullscreen:
                    window = pygame.display.set_mode((0, 0), FULLSCREEN)
                else:
                    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
            continue
        
        # Ayarlar menüsü state kontrolü
        elif game.state == "settings":
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    game.state = game.previous_state  # Geri dön
                    settings.save()
                    settings.apply_audio()
                elif ev.key == K_F11:
                    # Fullscreen toggle
                    game.fullscreen = not game.fullscreen
                    if game.fullscreen:
                        pygame.display.set_mode((SCREEN_W, SCREEN_H), FULLSCREEN)
                    else:
                        pygame.display.set_mode((SCREEN_W, SCREEN_H))
            elif ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                mx, my = transform_mouse_pos(ev.pos)
                # Dil butonları
                lang_tr_btn = pygame.Rect(SCREEN_W//2 - 180, SCREEN_H//2 - 130, 150, 50)
                lang_en_btn = pygame.Rect(SCREEN_W//2 + 30, SCREEN_H//2 - 130, 150, 50)
                # Geri butonu
                back_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 170, 250, 70)
                
                if lang_tr_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    settings.language = "TR"
                elif lang_en_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    settings.language = "EN"
                elif back_btn.collidepoint(mx, my):
                    game.state = game.previous_state  # Geri dön
                    settings.save()
                    settings.apply_audio()
                else:
                    # Slider kontrolü
                    sound_area = pygame.Rect(SCREEN_W//2 - 100, SCREEN_H//2 - 35, 300, 30)
                    music_area = pygame.Rect(SCREEN_W//2 - 100, SCREEN_H//2 + 45, 300, 30)
                    if sound_area.collidepoint(mx, my):
                        game.settings_slider = "sound"
                    elif music_area.collidepoint(mx, my):
                        game.settings_slider = "music"
            elif ev.type == MOUSEMOTION and game.settings_slider:
                mx, my = transform_mouse_pos(ev.pos)
                if game.settings_slider == "sound":
                    # Ses slider
                    sound_area = pygame.Rect(SCREEN_W//2 - 100, SCREEN_H//2 - 30, 300, 15)
                    if sound_area.collidepoint(mx, my):
                        settings.sound_volume = max(0.0, min(1.0, (mx - sound_area.x) / sound_area.w))
                elif game.settings_slider == "music":
                    # Müzik slider
                    music_area = pygame.Rect(SCREEN_W//2 - 100, SCREEN_H//2 + 50, 300, 15)
                    if music_area.collidepoint(mx, my):
                        new_vol = max(0.0, min(1.0, (mx - music_area.x) / music_area.w))
                        settings.music_volume = new_vol
                        settings.apply_audio()
            elif ev.type == MOUSEBUTTONUP and ev.button == 1:
                if game.settings_slider:
                    game.settings_slider = None
                    settings.save()
            continue
        
        # Nasıl Oynanır state kontrolü
        elif game.state == "howto":
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    game.state = game.previous_state  # Geri dön
                elif ev.key == K_F11:
                    # Fullscreen toggle
                    game.fullscreen = not game.fullscreen
                    if game.fullscreen:
                        window = pygame.display.set_mode((0, 0), FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
            elif ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                mx, my = transform_mouse_pos(ev.pos)
                # Geri butonu
                back_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 170, 250, 70)
                if back_btn.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    game.state = game.previous_state  # Geri dön
            continue

        elif ev.type == KEYDOWN:
            if ev.key == K_F11:
                # Fullscreen toggle
                game.fullscreen = not game.fullscreen
                if game.fullscreen:
                    window = pygame.display.set_mode((0, 0), FULLSCREEN)
                else:
                    window = pygame.display.set_mode((SCREEN_W, SCREEN_H))
            elif ev.key == K_ESCAPE:
                if game.state == "playing":
                    # Oyunu duraklat
                    game.pause_start_time = time.time()  # Duraklama başlangıç zamanını kaydet
                    game.state = "menu"
            elif ev.key == K_r:
                game.restart()
            elif ev.key == K_u:
                game.board.undo()

        elif ev.type == MOUSEBUTTONDOWN and ev.button == 1:
            mx,my = transform_mouse_pos(ev.pos)
            # Ayarlar butonu (sağ üst)
            if game.state == "playing":
                settings_btn_rect = pygame.Rect(SCREEN_W - 60, 10, 50, 50)
                if settings_btn_rect.collidepoint(mx, my):
                    play_sound(SND_CLICK)
                    game.previous_state = "playing"  # Oyun içinden ayarlara git
                    game.state = "settings"
                    continue
            
            # pick topmost block with padded hitbox
            for b in reversed(list(game.board.blocks.values())):
                if point_in_block_with_padding(b, mx, my):
                    game.selected = b
                    game.dragging = True
                    # attach drag helpers
                    b.drag_start_px = (mx, my)
                    b.axis_locked = None
                    b.offset = (mx - b.rect.x, my - b.rect.y)
                    # pixel_target'ı mevcut pozisyona eşitle
                    b.pixel_target = (b.rect.x, b.rect.y)
                    # save logical state
                    game.board.save()
                    # prepare preview
                    game.preview_cell = None
                    break

        elif ev.type == MOUSEMOTION:
            if game.dragging and game.selected:
                mx, my = transform_mouse_pos(ev.pos)
                b = game.selected
                sx, sy = b.drag_start_px
                dx_total = mx - sx
                dy_total = my - sy
                
                # Axis lock belirle
                if b.axis_locked is None:
                    if abs(dx_total) >= DRAG_THRESHOLD or abs(dy_total) >= DRAG_THRESHOLD:
                        b.axis_locked = 'x' if abs(dx_total) > abs(dy_total) else 'y'
                
                # Grid snap ile smooth sürükleme
                if b.axis_locked == 'x':
                    # Yatay hareket
                    new_x = mx - b.offset[0]
                    target_gx = int((new_x - MARGIN) // CELL_W)
                    target_gx = max(0, min(game.board.cols - b.w, target_gx))
                    target_x = MARGIN + target_gx * CELL_W
                    b.rect.x = target_x
                    b.rect.y = MARGIN + 120 + b.y * CELL_H
                elif b.axis_locked == 'y':
                    # Dikey hareket
                    new_y = my - b.offset[1]
                    target_gy = int((new_y - MARGIN - 120) // CELL_H)
                    target_gy = max(0, min(game.board.rows - b.h, target_gy))
                    target_y = MARGIN + 120 + target_gy * CELL_H
                    b.rect.y = target_y
                    b.rect.x = MARGIN + b.x * CELL_W
                else:
                    # Henüz lock olmadı - mouse'u takip et
                    b.rect.x = mx - b.offset[0]
                    b.rect.y = my - b.offset[1]
                    min_x = MARGIN
                    max_x = MARGIN + (game.board.cols - b.w) * CELL_W
                    min_y = MARGIN + 120
                    max_y = MARGIN + 120 + (game.board.rows - b.h) * CELL_H
                    b.rect.x = max(min_x, min(max_x, b.rect.x))
                    b.rect.y = max(min_y, min(max_y, b.rect.y))
                
                b.pixel_target = (b.rect.x, b.rect.y)
                # Preview hesapla - use top-left corner instead of center for correct positioning
                pgx, pgy = pixel_to_grid_center(b.rect.x, b.rect.y, b)
                game.preview_cell = (b.id, pgx, pgy)

        elif ev.type == MOUSEBUTTONUP and ev.button == 1:
            if game.dragging and game.selected:
                b = game.selected
                # Şu anki grid konumunu hesapla
                current_gx = int((b.rect.x - MARGIN) // CELL_W)
                current_gy = int((b.rect.y - MARGIN - 120) // CELL_H)
                
                # Grid pozisyonundan hareket miktarını hesapla
                dx = current_gx - b.x
                dy = current_gy - b.y
                
                moved = False
                
                # Eğer hareket yoksa, sadece visual'ı geri döndür
                if dx == 0 and dy == 0:
                    for bl in game.board.blocks.values():
                        bl.update_rect()
                        bl.pixel_target = (bl.rect.x, bl.rect.y)
                else:
                    # Hareket var - axis lock'a göre hareket et
                    if b.axis_locked == 'x' or (b.axis_locked is None and abs(dx) >= abs(dy)):
                        # Yatay hareket
                        step = 1 if dx > 0 else -1
                    for _ in range(abs(dx)):
                            if game.board.can_move(b.id, step, 0):
                                game.board.slide_one(b.id, step, 0, record=False)
                            moved = True
                        else:
                            break
                else:
                        # Dikey hareket
                        step = 1 if dy > 0 else -1
                    for _ in range(abs(dy)):
                            if game.board.can_move(b.id, 0, step):
                                game.board.slide_one(b.id, 0, step, record=False)
                            moved = True
                        else:
                            break
                
                if moved:
                    play_sound(SND_MOVE)
                    game.moves += 1
                    # Hareketten sonra tüm blokların rect'lerini güncelle
                    for bl in game.board.blocks.values():
                        bl.update_rect()
                        bl.pixel_target = (bl.rect.x, bl.rect.y)
                else:
                    # revert to saved state if no move
                    play_sound(SND_ERROR)
                    game.board.undo()
                    # Undo sonrası da tüm blokların rect'lerini güncelle
                    for bl in game.board.blocks.values():
                        bl.update_rect()
                        bl.pixel_target = (bl.rect.x, bl.rect.y)
                game.selected = None
                game.dragging = False
                game.preview_cell = None
                # solved?
                if game.board.is_solved() and not game.solved:
                    play_sound(SND_COMPLETE)
                    game.solved = True
                    game.completion_time = time.time() - game.start_time

    # animate all blocks towards their pixel targets (except if currently being dragged)
    if game.state == "playing":
            if game.dragging and game.selected:
            # Sadece sürüklenmeyen blokları animate et
            for bl in game.board.blocks.values():
                if bl is not game.selected:
                    bl.animate_towards_pixel_target(dt=dt)
                else:
            # Tüm blokları animate et
            for bl in game.board.blocks.values():
                bl.animate_towards_pixel_target(dt=dt)

    # DRAW
    screen.fill(BG)

    # Menü ekranı
    if game.state == "menu":
        # Başlık - Daha büyük
        title_y = SCREEN_H // 2 - 200
        menu_title_font = pygame.font.Font(bytesized_font_path, 56) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 56)
        title_text = menu_title_font.render("Klo.", True, TEXT)
        screen.blit(title_text, (SCREEN_W//2 - title_text.get_width()//2, title_y))
        
        menu_btn_font = pygame.font.Font(bytesized_font_path, 32) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 32)
        
        # "Oyna" butonu - Retro styled (softer)
        play_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 100, 250, 70)
        play_color = (0, 140, 80) if game.hovered_button == "play" else (0, 90, 50)
        pygame.draw.rect(screen, play_color, play_btn, border_radius=8)
        # Softer border
        pygame.draw.rect(screen, (0, 180, 100), play_btn, width=3, border_radius=8)
        if game.hovered_button == "play":
            # Subtle glow effect
            for i in range(2):
                glow_rect = pygame.Rect(play_btn.x - i, play_btn.y - i, play_btn.w + 2*i, play_btn.h + 2*i)
                pygame.draw.rect(screen, (0, 160, 90), glow_rect, width=1, border_radius=8)
        btn_text = menu_btn_font.render(get_text("menu_play"), True, (0, 200, 120))
        screen.blit(btn_text, (play_btn.centerx - btn_text.get_width()//2, play_btn.centery - btn_text.get_height()//2))
        
        # "Nasıl Oynanır" butonu
        howto_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 - 25, 250, 70)
        howto_color = (0, 140, 80) if game.hovered_button == "howto" else (0, 90, 50)
        pygame.draw.rect(screen, howto_color, howto_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), howto_btn, width=3, border_radius=8)
        if game.hovered_button == "howto":
            for i in range(2):
                glow_rect = pygame.Rect(howto_btn.x - i, howto_btn.y - i, howto_btn.w + 2*i, howto_btn.h + 2*i)
                pygame.draw.rect(screen, (0, 160, 90), glow_rect, width=1, border_radius=8)
        btn_text_howto = menu_btn_font.render(get_text("menu_howto"), True, (0, 200, 120))
        screen.blit(btn_text_howto, (howto_btn.centerx - btn_text_howto.get_width()//2, howto_btn.centery - btn_text_howto.get_height()//2))
        
        # "Ayarlar" butonu
        settings_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 50, 250, 70)
        settings_color = (0, 140, 80) if game.hovered_button == "settings" else (0, 90, 50)
        pygame.draw.rect(screen, settings_color, settings_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), settings_btn, width=3, border_radius=8)
        if game.hovered_button == "settings":
            for i in range(2):
                glow_rect = pygame.Rect(settings_btn.x - i, settings_btn.y - i, settings_btn.w + 2*i, settings_btn.h + 2*i)
                pygame.draw.rect(screen, (0, 160, 90), glow_rect, width=1, border_radius=8)
        btn_text_set = menu_btn_font.render(get_text("menu_settings"), True, (0, 200, 120))
        screen.blit(btn_text_set, (settings_btn.centerx - btn_text_set.get_width()//2, settings_btn.centery - btn_text_set.get_height()//2))
        
        # "Çıkış" butonu
        exit_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 125, 250, 70)
        exit_color = (180, 40, 40) if game.hovered_button == "exit" else (120, 30, 30)
        pygame.draw.rect(screen, exit_color, exit_btn, border_radius=8)
        pygame.draw.rect(screen, (200, 80, 80), exit_btn, width=3, border_radius=8)
        if game.hovered_button == "exit":
            for i in range(2):
                glow_rect = pygame.Rect(exit_btn.x - i, exit_btn.y - i, exit_btn.w + 2*i, exit_btn.h + 2*i)
                pygame.draw.rect(screen, (190, 70, 70), glow_rect, width=1, border_radius=8)
        btn_text2 = menu_btn_font.render(get_text("menu_exit"), True, (220, 140, 140))
        screen.blit(btn_text2, (exit_btn.centerx - btn_text2.get_width()//2, exit_btn.centery - btn_text2.get_height()//2))
        
        present()
        continue
    
    # Ayarlar ekranı
    if game.state == "settings":
        # Başlık
        title_y = SCREEN_H // 2 - 280
        menu_title_font = pygame.font.Font(bytesized_font_path, 44) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 44)
        title_text = menu_title_font.render(get_text("settings_title"), True, TEXT)
        screen.blit(title_text, (SCREEN_W//2 - title_text.get_width()//2, title_y))
        
        menu_btn_font = pygame.font.Font(bytesized_font_path, 24) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 24)
        
        # Dil Seçimi
        draw_text(screen, get_text("settings_language"), (SCREEN_W//2 - 150, SCREEN_H//2 - 180), font)
        lang_tr_btn = pygame.Rect(SCREEN_W//2 - 180, SCREEN_H//2 - 130, 150, 50)
        lang_en_btn = pygame.Rect(SCREEN_W//2 + 30, SCREEN_H//2 - 130, 150, 50)
        
        # TR butonu - Retro styled (softer)
        tr_color = (0, 140, 80) if settings.language == "TR" else (0, 70, 40)
        pygame.draw.rect(screen, tr_color, lang_tr_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), lang_tr_btn, width=3, border_radius=8)
        btn_tr = menu_btn_font.render(get_text("settings_turkish"), True, (0, 200, 120))
        screen.blit(btn_tr, (lang_tr_btn.centerx - btn_tr.get_width()//2, lang_tr_btn.centery - btn_tr.get_height()//2))
        
        # EN butonu - Retro styled (softer)
        en_color = (0, 140, 80) if settings.language == "EN" else (0, 70, 40)
        pygame.draw.rect(screen, en_color, lang_en_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), lang_en_btn, width=3, border_radius=8)
        btn_en = menu_btn_font.render(get_text("settings_english"), True, (0, 200, 120))
        screen.blit(btn_en, (lang_en_btn.centerx - btn_en.get_width()//2, lang_en_btn.centery - btn_en.get_height()//2))
        
        # Ses Efektleri Seviyesi - Retro slider (softer)
        draw_text(screen, get_text("settings_sound"), (SCREEN_W//2 - 150, SCREEN_H//2 - 50), font)
        sound_x = SCREEN_W//2 - 100
        sound_y = SCREEN_H//2 - 30
        sound_w = 300
        sound_h = 20
        sound_slider = pygame.Rect(sound_x, sound_y, int(sound_w * settings.sound_volume), sound_h)
        pygame.draw.rect(screen, (40, 80, 50), (sound_x, sound_y, sound_w, sound_h), border_radius=4)
        pygame.draw.rect(screen, (0, 180, 100), sound_slider, border_radius=4)
        pygame.draw.rect(screen, (0, 160, 90), (sound_x, sound_y, sound_w, sound_h), width=2, border_radius=4)
        
        # Müzik Seviyesi - Retro slider (softer)
        draw_text(screen, get_text("settings_music"), (SCREEN_W//2 - 150, SCREEN_H//2 + 30), font)
        music_x = SCREEN_W//2 - 100
        music_y = SCREEN_H//2 + 50
        music_w = 300
        music_h = 20
        music_slider = pygame.Rect(music_x, music_y, int(music_w * settings.music_volume), music_h)
        pygame.draw.rect(screen, (40, 80, 50), (music_x, music_y, music_w, music_h), border_radius=4)
        pygame.draw.rect(screen, (0, 180, 100), music_slider, border_radius=4)
        pygame.draw.rect(screen, (0, 160, 90), (music_x, music_y, music_w, music_h), width=2, border_radius=4)
        
        # Geri butonu - Retro styled (softer)
        back_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 170, 250, 70)
        back_color = (0, 90, 50)
        pygame.draw.rect(screen, back_color, back_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), back_btn, width=3, border_radius=8)
        btn_back = menu_btn_font.render(get_text("settings_back"), True, (0, 200, 120))
        screen.blit(btn_back, (back_btn.centerx - btn_back.get_width()//2, back_btn.centery - btn_back.get_height()//2))
        
        present()
        continue
    
    # Nasıl Oynanır ekranı
    if game.state == "howto":
        # Başlık
        title_y = SCREEN_H // 2 - 280
        menu_title_font = pygame.font.Font(bytesized_font_path, 44) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 44)
        title_text = menu_title_font.render(get_text("howto_title"), True, TEXT)
        screen.blit(title_text, (SCREEN_W//2 - title_text.get_width()//2, title_y))
        
        menu_btn_font = pygame.font.Font(bytesized_font_path, 24) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 24)
        
        y_start = SCREEN_H // 2 - 200
        line_spacing = 35
        
        # Amaç bölümü
        draw_text(screen, get_text("howto_objective"), (SCREEN_W//2 - 200, y_start), font)
        draw_text(screen, get_text("howto_objective_text"), (SCREEN_W//2 - 200, y_start + 30), font)
        
        # Kontroller bölümü
        draw_text(screen, get_text("howto_controls"), (SCREEN_W//2 - 200, y_start + 80), font)
        
        current_y = y_start + 110
        draw_text(screen, get_text("howto_mouse"), (SCREEN_W//2 - 200, current_y), font)
        current_y += line_spacing
        draw_text(screen, get_text("howto_u"), (SCREEN_W//2 - 200, current_y), font)
        current_y += line_spacing
        draw_text(screen, get_text("howto_r"), (SCREEN_W//2 - 200, current_y), font)
        current_y += line_spacing
        draw_text(screen, get_text("howto_esc"), (SCREEN_W//2 - 200, current_y), font)
        current_y += line_spacing
        draw_text(screen, get_text("howto_f11"), (SCREEN_W//2 - 200, current_y), font)
        
        # Geri butonu - Retro styled (softer)
        back_btn = pygame.Rect(SCREEN_W//2 - 125, SCREEN_H//2 + 170, 250, 70)
        back_color = (0, 90, 50)
        pygame.draw.rect(screen, back_color, back_btn, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), back_btn, width=3, border_radius=8)
        btn_back = menu_btn_font.render(get_text("howto_back"), True, (0, 200, 120))
        screen.blit(btn_back, (back_btn.centerx - btn_back.get_width()//2, back_btn.centery - btn_back.get_height()//2))
        
        present()
        continue
    
    # Oyun ekranı
    if game.state == "playing":
        # Ayarlar butonu (sağ üst) - Retro styled (softer)
        settings_btn_rect = pygame.Rect(SCREEN_W - 60, 10, 50, 50)
        pygame.draw.rect(screen, (0, 90, 50), settings_btn_rect, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), settings_btn_rect, width=2, border_radius=8)
        settings_icon_font = pygame.font.Font(bytesized_font_path, 24) if os.path.exists(bytesized_font_path) else pygame.font.Font(None, 24)
        settings_icon = settings_icon_font.render("⚙", True, (0, 200, 120))
        screen.blit(settings_icon, (settings_btn_rect.centerx - settings_icon.get_width()//2, settings_btn_rect.centery - settings_icon.get_height()//2))
        
        draw_text(screen, "Klo.", (MARGIN + 20, 34), titlefont)
        elapsed_time = (time.time() - game.start_time - game.paused_duration) if not game.solved else game.completion_time
        minutes = int(elapsed_time // 60); seconds = int(elapsed_time % 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        draw_text(screen, f"{get_text('game_moves')}: {game.moves}   {get_text('game_time')}: {time_str}", (MARGIN + 20, 74), font)
        
        # Müzik bilgisi - Sol alta
        if game.current_music:
            # Müzik dosya isminden yapımcı adını çıkar (örnek: "DavidKBD - Pink Bloom Pack - 01 - Pink Bloom.ogg")
            file_name = game.current_music.get('file', '')
            producer = "Unknown"
            if ' - ' in file_name:
                producer = file_name.split(' - ')[0]
            music_text = f"♪ {game.current_music['name']} - {producer}"
            draw_text(screen, music_text, (MARGIN + 20, SCREEN_H - 30), font)

        # board background
    pygame.draw.rect(screen, BOARD_BG, (MARGIN, MARGIN+120, BOARD_W, BOARD_H), border_radius=10)

        # grid lines
    for i in range(1, game.board.cols):
            x = MARGIN + i * CELL_W
        pygame.draw.line(screen, GRID_LINE, (x, MARGIN+120), (x, MARGIN+120+BOARD_H), 2)
    for j in range(1, game.board.rows):
            y = MARGIN + 120 + j * CELL_H
        pygame.draw.line(screen, GRID_LINE, (MARGIN, y), (MARGIN+BOARD_W, y), 2)

        # exit marker - Retro styled with subtle glow
    ex,ey = game.board.exit
        ex_r = pygame.Rect(MARGIN + ex * CELL_W, MARGIN + 120 + ey * CELL_H, CELL_W * 2, CELL_H * 2)
        # Subtle glow effect
        for i in range(1):
            glow_r = pygame.Rect(ex_r.x - i, ex_r.y - i, ex_r.w + 2*i, ex_r.h + 2*i)
            pygame.draw.rect(screen, (0, 140, 70), glow_r, border_radius=8 + i)
        pygame.draw.rect(screen, (0, 160, 90), ex_r, border_radius=8)
        pygame.draw.rect(screen, (0, 180, 100), ex_r, width=2, border_radius=8)
        draw_text(screen, get_text("game_exit"), (ex_r.x + 6, ex_r.y + 6), font)

        # preview outline - Retro styled with subtle glow
        if getattr(game, "preview_cell", None) is not None:
            pid, pgx, pgy = game.preview_cell
            preview_block = game.board.blocks.get(pid)
            if preview_block:
                preview_rect = pygame.Rect(MARGIN + pgx * CELL_W, MARGIN + 120 + pgy * CELL_H, CELL_W * preview_block.w, CELL_H * preview_block.h)
                # Subtle glow effect
                pygame.draw.rect(screen, (0, 160, 100), preview_rect, width=3, border_radius=12)

        # draw blocks (non-selected first) - sadece grid pozisyonlarında
        for bl in game.board.blocks.values():
            if bl is game.selected: continue
            # Grid pozisyonunda göster
            saved_rect = bl.rect
            bl.rect = pygame.Rect(MARGIN + bl.x * CELL_W, MARGIN + 120 + bl.y * CELL_H, bl.rect.w, bl.rect.h)
            bl.draw(screen)
            bl.rect = saved_rect
        
        # Sürüklenen bloğu en sonda çiz, biraz yukarıda (elevation) çiz ki diğer blokların üstünde görünsün
    if game.selected:
            elev = 20  # Yukarıda çizmek için offset
            original_y = game.selected.rect.y
            # Sürüklenen blok grid'in dışına çıkmasın
            min_y = MARGIN + 120
            game.selected.rect.y = max(min_y, original_y - elev)
        game.selected.draw(screen, dragging=True)
            # Geri döndür
            game.selected.rect.y = original_y

        # completion overlay - Retro styled (softer)
        if game.solved:
            overlay = pygame.Surface((SCREEN_W, SCREEN_H))
            overlay.set_alpha(200)
            overlay.fill((10,10,10))
            screen.blit(overlay, (0,0))
            # Softer victory colors
            draw_text(screen, get_text("game_complete"), (SCREEN_W//2 - 80, SCREEN_H//2 - 100), titlefont, (220, 220, 120))  # Softer yellow
            completion_minutes = int(game.completion_time // 60)
            completion_seconds = int(game.completion_time % 60)
            draw_text(screen, f"{get_text('game_complete_time')}: {completion_minutes:02d}:{completion_seconds:02d}", (SCREEN_W//2 - 140, SCREEN_H//2 - 40), bigfont, (0, 200, 120))
            draw_text(screen, f"{get_text('game_complete_moves')}: {game.moves}", (SCREEN_W//2 - 100, SCREEN_H//2 + 20), bigfont, (0, 200, 120))
            draw_text(screen, get_text("game_restart_hint"), (SCREEN_W//2 - 120, SCREEN_H//2 + 100), font, (100, 200, 140))


    present()

pygame.quit()
sys.exit()
