import tkinter as tk
from tkinter import ttk, messagebox
import random

APP_TITLE = "Arcana — Tarot Reader"

MAJORS = [
("The Fool","new beginnings, openness, spontaneity, a leap of faith","recklessness, hesitation, needless risk, fear of the unknown","A fresh chapter is available. Stay curious, but take one grounded step rather than leaping blindly."),
("The Magician","initiative, resourcefulness, focused intention, making things happen","scattered energy, manipulation, unused potential, poor planning","You have more tools than you may realize. Focus your attention and turn an idea into a concrete action."),
("The High Priestess","intuition, inner knowing, mystery, patience","ignoring intuition, hidden information, emotional noise","Slow down and listen. Not every answer is available through logic alone; give yourself quiet to notice what you know."),
("The Empress","nurturing, creativity, abundance, comfort, growth","smothering, creative block, neglecting your own needs","Create conditions in which people and projects can flourish. Care for yourself as generously as you care for others."),
("The Emperor","structure, boundaries, leadership, stability","rigidity, domination, disorder, inflexible rules","A clear plan and healthy boundaries can help. Lead responsibly without confusing control with security."),
("The Hierophant","tradition, learning, shared values, mentorship","questioning convention, restrictive beliefs, nonconformity","Seek wisdom from a trusted teacher or practice, while deciding which traditions genuinely fit your values."),
("The Lovers","connection, alignment, meaningful choice, mutual respect","misalignment, indecision, imbalance, values in conflict","Choose in a way that reflects your values. Honest communication matters more than trying to please everyone."),
("The Chariot","determination, direction, self-discipline, momentum","loss of direction, forcefulness, conflicting impulses","Progress comes from steering competing forces toward one goal. Set a direction and keep your attention there."),
("Strength","courage, patience, compassion, quiet confidence","self-doubt, frustration, harshness, depleted energy","Gentle persistence is stronger than force. Meet a difficult feeling with compassion and steady resolve."),
("The Hermit","reflection, solitude, inner guidance, thoughtful study","isolation, withdrawal, avoiding advice, loneliness","Step back long enough to hear your own judgment. Solitude helps when it restores perspective rather than shutting everyone out."),
("Wheel of Fortune","change, cycles, turning points, unexpected opportunity","resistance to change, unstable timing, repeating patterns","Circumstances are moving. Notice what is outside your control and make the most of the choices still available to you."),
("Justice","fairness, truth, accountability, balanced decisions","bias, avoidance of responsibility, unfairness","Look at the facts and your own part in the situation. A fair decision requires honesty, proportion, and accountability."),
("The Hanged Man","pause, surrender, new perspective, patience","stagnation, needless sacrifice, resisting a pause","A delay may be useful if it changes how you see the problem. Release the urge to force an answer before you are ready."),
("Death","ending, transition, release, transformation","clinging to the past, fear of change, unfinished closure","Something may need to end so something else can begin. Let go of what has run its course; this card does not predict literal death."),
("Temperance","moderation, integration, healing, cooperation","excess, impatience, imbalance, incompatible priorities","Find a sustainable middle path. Small adjustments and cooperation can bring apparently competing needs into balance."),
("The Devil","attachment, temptation, unhealthy patterns, material fixation","recognizing a pattern, reclaiming agency, loosening a bond","Notice where fear, habit, or desire has narrowed your choices. Naming a pattern is the first step toward changing it."),
("The Tower","sudden revelation, disruption, truth breaking through","avoided upheaval, fear of change, gradual breakdown","A shaky assumption may be challenged. Face what is real and rebuild on firmer ground rather than preserving appearances."),
("The Star","hope, renewal, openness, inspiration","discouragement, disconnection, fading confidence","Recovery and renewed perspective are possible. Make room for rest, honesty, and one small source of hope."),
("The Moon","uncertainty, dreams, intuition, unclear information","confusion lifting, fear exposed, misread signals","Not everything is as clear as it seems. Verify assumptions, attend to feelings, and wait for more information before deciding."),
("The Sun","joy, vitality, clarity, success, warmth","temporary cloudiness, overconfidence, delayed optimism","Let yourself recognize what is working. Share your energy, celebrate progress, and keep expectations realistic."),
("Judgement","awakening, reflection, renewal, answering a call","harsh self-judgment, avoidance, reluctance to change","Review the past honestly without being trapped by it. You can learn from what happened and choose a more aligned next step."),
("The World","completion, integration, achievement, a meaningful cycle ending","unfinished business, delays, difficulty moving on","A cycle is approaching completion. Recognize what you have learned, close remaining loops, and prepare for the next chapter."),
]

# Minor Arcana ranks and their broad interpretive themes.
RANKS = [
("Ace","beginnings, potential, a fresh opportunity","missed opening, blocked potential, hesitation"),
("Two","choice, balance, partnership, planning","indecision, imbalance, competing priorities"),
("Three","growth, collaboration, expression, early results","delays, miscommunication, lack of teamwork"),
("Four","stability, rest, foundations, consolidation","stagnation, restlessness, unstable foundations"),
("Five","challenge, friction, change through difficulty","recovery, conflict avoidance, lingering tension"),
("Six","progress, support, generosity, moving forward","unfinished transition, one-sided giving, setbacks"),
("Seven","assessment, perseverance, strategy, standing firm","doubt, poor strategy, giving up too soon"),
("Eight","movement, practice, momentum, focused effort","frustration, scattered effort, delays"),
("Nine","near-completion, independence, resilience","weariness, overextension, insecurity"),
("Ten","culmination, responsibility, completion","burden, excess, difficulty letting go"),
("Page","curiosity, messages, learning, a beginner's mind","immaturity, unreliable news, lack of follow-through"),
("Knight","pursuit, action, ambition, movement","impulsiveness, inconsistency, misplaced intensity"),
("Queen","mature understanding, care, inner mastery","insecurity, imbalance, withholding or overgiving"),
("King","leadership, command, stewardship, mastery","rigidity, misuse of authority, poor self-management"),
]
SUITS = [
("Wands","fire","passion, creativity, ambition, initiative","burnout, impatience, scattered motivation","This card emphasizes what energizes you: creative action, courage, and the way you direct your ambition."),
("Cups","water","emotion, relationships, empathy, imagination","emotional overwhelm, withdrawal, blurred boundaries","This card emphasizes feelings and connection. Make space for emotional honesty while keeping healthy boundaries."),
("Swords","air","thought, communication, truth, decisions","overthinking, conflict, confusion, harsh words","This card emphasizes the mind and communication. Seek clarity, test assumptions, and use words with care."),
("Pentacles","earth","work, resources, health routines, practical stability","scarcity, stagnation, material stress, neglect of basics","This card emphasizes practical life: resources, work, routines, and the patient effort that builds stability."),
]

CARDS = []
for name, up, rev, advice in MAJORS:
    CARDS.append({"name":name,"arcana":"Major Arcana","upright":up,"reversed":rev,"advice":advice,"symbol":"A major life theme or important inner lesson is highlighted."})
for suit, element, suit_up, suit_rev, suit_advice in SUITS:
    for rank, rank_up, rank_rev in RANKS:
        name = f"{rank} of {suit}"
        # Combine suit and rank themes into an interpretation that remains distinct for all 56 cards.
        CARDS.append({
            "name":name,"arcana":"Minor Arcana",
            "upright":f"{rank_up}; {suit_up}",
            "reversed":f"{rank_rev}; {suit_rev}",
            "advice":f"{suit_advice} Consider how '{rank_up}' applies to the situation in front of you, and choose one practical step that reflects it.",
            "symbol":f"The suit of {suit.lower()} is associated with {suit_up}. Its {rank.lower()} expresses a particular stage or approach: {rank_up}."
        })

SPREADS = {
    "One Card": ["Your card"],
    "Three Cards — Past / Present / Future": ["Past","Present","Future"],
    "Celtic Cross — 10 Cards": ["Present situation","Challenge / crossing influence","Root cause","Recent past","Conscious aim / best possibility","Near future","Your approach","External influences","Hopes and fears","Likely direction"],
}

class TarotApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1000x760")
        self.root.minsize(820, 620)
        self.root.configure(bg="#171426")
        self.cards_in_reading = []
        self.dark_theme = True  # toggle_theme() after construction applies the light default
        self.shadow_var = tk.BooleanVar(value=False)
        self._style()
        self._build()

    def _style(self):
        style = ttk.Style()
        try: style.theme_use("clam")
        except tk.TclError: pass
        style.configure("TCombobox", padding=6)
        style.configure("TButton", padding=8, font=("Segoe UI", 10, "bold"))

    def _build(self):
        header = tk.Frame(self.root, bg="#171426", padx=24, pady=18)
        header.pack(fill="x")
        title_row = tk.Frame(header, bg="#171426")
        title_row.pack(fill="x")
        tk.Label(title_row, text="✦  ARCANA", font=("Georgia", 25, "bold"), fg="#f2d59b", bg="#171426").pack(side="left", anchor="w")
        self.theme_button = tk.Button(title_row, text="☀  Light theme", command=self.toggle_theme, font=("Segoe UI", 9, "bold"), relief="flat", padx=12, pady=7, cursor="hand2", bg="#eee9f5", fg="#241f38", activebackground="#ddd4eb")
        self.theme_button.pack(side="right")
        tk.Label(header, text="A 78-card tarot reader · reflective guidance, not fixed prediction", font=("Segoe UI", 10), fg="#c8bfdc", bg="#171426").pack(anchor="w", pady=(3, 0))

        controls = tk.Frame(self.root, bg="#241f38", padx=20, pady=14)
        controls.pack(fill="x", padx=20)
        tk.Label(controls, text="SPREAD", font=("Segoe UI", 9, "bold"), fg="#d8c9f0", bg="#241f38").pack(side="left", padx=(0, 10))
        self.spread_var = tk.StringVar(value="Three Cards — Past / Present / Future")
        self.spread_combo = ttk.Combobox(controls, textvariable=self.spread_var, values=list(SPREADS.keys()), state="readonly", width=36)
        self.spread_combo.pack(side="left")
        ttk.Button(controls, text="Draw Reading", command=self.draw).pack(side="left", padx=12)
        ttk.Button(controls, text="Clear", command=self.clear).pack(side="left")
        tk.Checkbutton(controls, text="Shadow reading (ominous fictional interpretations)", variable=self.shadow_var, bg="#241f38", fg="#d8c9f0", selectcolor="#171426", activebackground="#241f38", activeforeground="#ffffff").pack(side="left", padx=(12, 0))
        tk.Label(controls, text="Cards are drawn without replacement within each spread.", font=("Segoe UI", 9), fg="#b7accb", bg="#241f38").pack(side="right", padx=4)

        self.summary = tk.Label(self.root, text="Choose a spread, take a breath, and draw your cards.", wraplength=920, justify="left", font=("Segoe UI", 11), fg="#f0eaf8", bg="#171426", padx=24, pady=15)
        self.summary.pack(fill="x")

        body = tk.Frame(self.root, bg="#171426", padx=20, pady=0)
        body.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(body, bg="#171426", highlightthickness=0)
        scrollbar = ttk.Scrollbar(body, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.results = tk.Frame(self.canvas, bg="#171426")
        self.window_id = self.canvas.create_window((0, 0), window=self.results, anchor="nw")
        self.results.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfigure(self.window_id, width=e.width))
        self.canvas.bind_all("<MouseWheel>", self._wheel)

        footer = tk.Label(self.root, text="For reflection and entertainment. Tarot does not guarantee outcomes or replace professional advice.", font=("Segoe UI", 8), fg="#8f849f", bg="#171426", pady=10)
        footer.pack(fill="x")
        self.toggle_theme()  # initialize the interface in light theme

    def toggle_theme(self):
        """Switch the interface palette only; reading tone is controlled separately."""
        self.dark_theme = not self.dark_theme
        light = {
            "#171426": "#f7f4fb", "#241f38": "#e9e2f2", "#29233d": "#ffffff",
            "#352a48": "#eee8f5", "#f2d59b": "#6d4a12", "#c8bfdc": "#514761",
            "#b7accb": "#514761", "#d8c9f0": "#443754", "#f0eaf8": "#292235",
            "#bdaed7": "#655477", "#d3c7e4": "#514761", "#8f849f": "#6d6478",
            "#54456c": "#d4c9e1", "#e7b5b5": "#963e4b"
        }
        dark = {
            "#f7f4fb": "#171426", "#e9e2f2": "#241f38", "#ffffff": "#29233d",
            "#eee8f5": "#352a48", "#6d4a12": "#f2d59b", "#514761": "#c8bfdc",
            "#443754": "#d8c9f0", "#292235": "#f0eaf8", "#655477": "#bdaed7",
            "#6d6478": "#8f849f", "#d4c9e1": "#54456c", "#963e4b": "#e7b5b5"
        }
        mapping = dark if self.dark_theme else light
        def recolor(widget):
            for option in ("bg", "background", "fg", "foreground", "highlightbackground", "activebackground", "activeforeground", "selectcolor"):
                try:
                    old = widget.cget(option)
                    if old in mapping:
                        widget.configure(**{option: mapping[old]})
                except (tk.TclError, TypeError):
                    pass
            for child in widget.winfo_children():
                recolor(child)
        recolor(self.root)
        self.root.configure(bg="#171426" if self.dark_theme else "#f7f4fb")
        self.canvas.configure(bg="#171426" if self.dark_theme else "#f7f4fb")
        self.theme_button.configure(text="☾  Dark theme" if self.dark_theme else "☀  Light theme")

    def _wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120), "units"))

    def clear(self):
        for child in self.results.winfo_children(): child.destroy()
        self.cards_in_reading = []
        self.summary.config(text="Choose a spread, take a breath, and draw your cards.")
        self.canvas.yview_moveto(0)

    def draw(self):
        self.clear()
        spread_name = self.spread_var.get()
        positions = SPREADS[spread_name]
        drawn = random.sample(CARDS, len(positions))
        self.cards_in_reading = []
        for i, (position, card) in enumerate(zip(positions, drawn)):
            reversed_card = random.choice([False, True])
            self.cards_in_reading.append((position, card, reversed_card))
        self._make_overview(spread_name)
        for i, (position, card, rev) in enumerate(self.cards_in_reading, 1):
            self._card_panel(i, position, card, rev)
        self._make_synthesis(spread_name)
        self.canvas.yview_moveto(0)

    def _make_overview(self, spread_name):
        names = [f"{c['name']}{' (Reversed)' if r else ''}" for _, c, r in self.cards_in_reading]
        self.summary.config(text=f"{spread_name}\nDrawn: " + "  ·  ".join(names) + "\n\nRead each card as a prompt for reflection. The future position describes a possible direction if current patterns continue—not a guaranteed event.")

    def _card_panel(self, number, position, card, reversed_card):
        panel = tk.Frame(self.results, bg="#29233d", padx=18, pady=15, highlightbackground="#54456c", highlightthickness=1)
        panel.pack(fill="x", pady=(0, 12), padx=2)
        orientation = "REVERSED" if reversed_card else "UPRIGHT"
        meaning = card["reversed"] if reversed_card else card["upright"]
        shadow_lines = [
            "A warning from the shadow: an ignored pattern may be tightening its grip. Pause before repeating it.",
            "Something unresolved casts a long shadow here. Look directly at the difficult truth instead of letting dread fill the gaps.",
            "The path ahead may feel narrow if old habits remain in control. This is a fictional prompt to reclaim your choices, not a prediction of harm.",
            "A fragile assumption may crack under pressure. Let what is unsteady be examined before you build further on it.",
            "This card evokes loss, uncertainty, or regret. Name the fear plainly, then choose one grounded action that protects your wellbeing."
        ]
        if self.shadow_var.get():
            meaning = "Shadow interpretation: " + random.choice(shadow_lines) + " Traditional theme: " + meaning
        accent = "#e7b5b5" if reversed_card else "#f2d59b"
        tk.Label(panel, text=f"{number:02d}  ·  {position.upper()}", font=("Segoe UI", 9, "bold"), fg="#bdaed7", bg="#29233d").pack(anchor="w")
        tk.Label(panel, text=card["name"] + ("  ↻" if reversed_card else "  ✦"), font=("Georgia", 18, "bold"), fg=accent, bg="#29233d").pack(anchor="w", pady=(4, 0))
        tk.Label(panel, text=f"{card['arcana']}  |  {orientation}", font=("Segoe UI", 9, "bold"), fg="#d3c7e4", bg="#29233d").pack(anchor="w", pady=(2, 8))
        self._text(panel, "MEANING", meaning)
        self._text(panel, "SYMBOLISM", card["symbol"])
        guidance = card["advice"]
        if self.shadow_var.get():
            guidance = "In this intentionally ominous, fictional reading, consider what could worsen if you keep avoiding the issue. This is a dramatic reflection prompt—not a forecast or evidence that something bad will happen. " + guidance
        self._text(panel, "GUIDANCE", guidance)

    def _text(self, parent, label, content):
        row = tk.Frame(parent, bg="#29233d")
        row.pack(fill="x", pady=(4, 0))
        tk.Label(row, text=label, font=("Segoe UI", 8, "bold"), fg="#bdaed7", bg="#29233d", width=12, anchor="nw").pack(side="left")
        tk.Label(row, text=content, font=("Segoe UI", 10), fg="#f0eaf8", bg="#29233d", justify="left", wraplength=760, anchor="w").pack(side="left", fill="x", expand=True)

    def _make_synthesis(self, spread_name):
        panel = tk.Frame(self.results, bg="#352a48", padx=18, pady=16)
        panel.pack(fill="x", pady=(2, 14), padx=2)
        tk.Label(panel, text="THE STORY OF YOUR READING", font=("Segoe UI", 10, "bold"), fg="#f2d59b", bg="#352a48").pack(anchor="w", pady=(0, 8))
        paragraphs = self._synthesis_text(spread_name)
        for p in paragraphs:
            tk.Label(panel, text=p, font=("Segoe UI", 10), fg="#f0eaf8", bg="#352a48", justify="left", wraplength=800, anchor="w").pack(fill="x", anchor="w", pady=(0, 8))

    def _synthesis_text(self, spread_name):
        items = self.cards_in_reading
        suit_counts = {s[0]: 0 for s in SUITS}
        majors = 0
        for _, c, _ in items:
            if c['arcana'] == 'Major Arcana': majors += 1
            else:
                for s, *_ in SUITS:
                    if c['name'].endswith(' of ' + s): suit_counts[s] += 1
        reversed_count = sum(1 for _, _, r in items if r)
        paragraphs = []
        if spread_name.startswith("Three Cards"):
            past, present, future = items
            past_meaning = past[1]["reversed"] if past[2] else past[1]["upright"]
            present_meaning = present[1]["reversed"] if present[2] else present[1]["upright"]
            future_meaning = future[1]["reversed"] if future[2] else future[1]["upright"]
            paragraphs.append("The thread from past to future: {} in the past position suggests {}. In the present, {} points to {}. The future position, {}, invites you to consider {}. Taken together, the spread asks how an earlier pattern is shaping today's choices—and what could shift if you respond consciously.".format(past[1]["name"], past_meaning, present[1]["name"], present_meaning, future[1]["name"], future_meaning))
        elif spread_name.startswith("Celtic Cross"):
            present, challenge, root, past, aim, future, selfcard, external, hopes, outcome = items
            paragraphs.append("The central tension is between {} (the present situation) and {} (the challenge). The root card, {}, suggests a deeper theme worth examining, while {} marks what may be receding. {} describes a conscious aim; {} offers a possible near-term direction. Your own approach appears in {}, while {} points to outside influences. Finally, {} reflects hopes or fears, and {} suggests a likely direction if the current pattern continues.".format(present[1]["name"], challenge[1]["name"], root[1]["name"], past[1]["name"], aim[1]["name"], future[1]["name"], selfcard[1]["name"], external[1]["name"], hopes[1]["name"], outcome[1]["name"]))
        else:
            pos, c, rev = items[0]
            focus_meaning = ("Reversed, it can point to " + c["reversed"]) if rev else ("Upright, it points to " + c["upright"])
            paragraphs.append("Your single-card focus is {}. {}. Use it as a lens for the situation you are considering: what feels accurate, what does not, and what small action could help you respond with intention?".format(c["name"], focus_meaning))
        if majors >= 3 or (len(items) <= 3 and majors >= 2):
            paragraphs.append("Several Major Arcana cards appear. In tarot tradition, that can emphasize larger life themes, turning points, or lessons of personal growth rather than only day-to-day details.")
        elif majors == 0:
            paragraphs.append("This spread is entirely Minor Arcana, which often keeps attention on everyday choices, relationships, work, resources, and the habits through which change happens.")
        if reversed_count >= max(2, len(items)//2):
            paragraphs.append("Many cards are reversed. You might read this as an invitation to look inward, reconsider assumptions, or notice where energy is blocked—not as a bad omen.")
        dominant = max(suit_counts, key=suit_counts.get) if suit_counts else None
        if dominant and suit_counts[dominant] >= 2:
            desc = {"Wands":"initiative and creative energy", "Cups":"emotions and relationships", "Swords":"thought and communication", "Pentacles":"practical matters and stability"}[dominant]
            paragraphs.append(f"The suit of {dominant} appears most often, bringing extra emphasis to {desc}.")
        paragraphs.append("A useful closing question: which part of this reading feels most relevant to your real circumstances, and what is one thoughtful, practical step you can take next? Keep what resonates, question what does not, and remember that your choices remain your own.")
        return paragraphs

if __name__ == '__main__':
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
