import streamlit as st
from datetime import datetime, date
import random

# ================= 1. 多语言字典 =================
TEXTS = {
    "中文": {
        "page_title": "多维命运轨迹解析仪",
        "title": "🌌 宇宙天象 · 多维命运轨迹解析仪",
        "subtitle": "输入出生信息，结合星象、天干地支、易经八卦，为你寻找历史上的**参照灵魂**。",
        "lang_label": "🌐 选择语言 (Language)",
        "birth_date": "**出生日期**",
        "year": "年", "month": "月", "day": "日",
        "address": "出生/现居地址（随便填，增加玄学氛围）",
        "address_default": "中国湖南娄底",
        "submit": "开始推演",
        "profile_title": "🔮 你的多维灵魂画像",
        "hexagram": "易经卦象", "ganzhi": "天干地支", "sign": "星座星象", "wuxing": "五行属性",
        "caption_calc": "（分析坐标：{}。系统已结合当日虚拟天象、天干磁场、易经卦象进行综合推演……）",
        "match_title": "📜 为你匹配的 3 位历史参照人物",
        "achievement": "**历史成就**：{}",
        "magnetic": "**人物磁场**：`{}` | `{}` | `五行属{}` | `易经:{}`",
        "expand_text": "展开查看【核心性格】与【人生轨迹】客观解析",
        "core_p": "**核心性格**：{}",
        "trajectory": "**人生轨迹**：{}",
        "success_reasons": "**系统推演命中以下玄学羁绊：**\n\n{}",
        "warning": "命运的齿轮在隐秘处转动，暂未发现强烈的直接羁绊……",
        "score": "综合共振指数：{} 点（仅供娱乐参考）",
        "footer": "注：本程序为趣味推演，历史人物的命运由时代与个人实践共同决定。数据解析旨在为你提供另一种认识自我的视角。",
        
        # 匹配理由文案
        "reason_zodiac": "**【生肖同源】**：你们同为{}年生肖，在东方命理中，这代表着底层的生命周期与运势节奏高度重合。",
        "reason_sign": "**【星象重叠】**：你们同为{}，受同一星象守护，在情感表达与潜意识层面存在强烈的共性。",
        "reason_element": "**【四象共鸣】**：你们同属于{}星座（{}与{}），意味着你们在感知世界和行动时的基本元素是一致的。",
        "reason_wuxing": "**【五行同频】**：你们的五行同属{}，这表明在生命能量的流动方式与处事风格上，你们有着相同的属性。",
        "reason_tiangan": "**【天干契合】**：你们的天干同为{}，在古代历法中，这意味着你们拥有相似的初始驱动力与性格底色。",
        "reason_hex": "**【卦象指引】**：你们的命理推演指向了同一卦象《{}》，这暗示你们在面对人生重大转折时，会做出相似的选择。",
        "vibe_1": "**【气场纠缠】**：结合{}行的能量场与{}卦的时空推演，你们在某种特定情境下的决策逻辑惊人地相似。",
        "vibe_2": "**【时代回音】**：虽然时代背景迥异，但你们的星盘轨迹在『{}』与当下的交汇处，呈现出一种奇妙的镜像关系。",
        "vibe_3": "**【灵魂暗合】**：古籍记载，同属{}体质的人，往往会在中晚年展现出与{}相似的坚韧与旷达。",
        "vibe_4": "**【磁场共振】**：你们的出生能量场（{} / {}）与该历史人物的生命图谱产生了微弱的量子共振。"
    },
    "English": {
        "page_title": "Destiny Analyzer",
        "title": "🌌 Cosmic Phenomena · Destiny Analyzer",
        "subtitle": "Enter your birth info. Using astrology, Ganzhi, and I Ching, we find your **historical soulmates**.",
        "lang_label": "🌐 Select Language (语言)",
        "birth_date": "**Date of Birth**",
        "year": "Year", "month": "Month", "day": "Day",
        "address": "Birth/Current Address (for mystical vibe)",
        "address_default": "Earth, Somewhere",
        "submit": "Start Analysis",
        "profile_title": "🔮 Your Multidimensional Soul Profile",
        "hexagram": "I Ching Hexagram", "ganzhi": "Ganzhi", "sign": "Zodiac Sign", "wuxing": "Five Elements",
        "caption_calc": "(Coordinates: {}. Calculated with virtual celestial phenomena, Ganzhi magnetic fields, and I Ching...)",
        "match_title": "📜 3 Historical Figures Matched for You",
        "achievement": "**Achievement**: {}",
        "magnetic": "**Magnetic Field**: `{}` | `{}` | `Element: {}` | `Hexagram: {}`",
        "expand_text": "Expand for Objective Analysis of [Personality] & [Life Path]",
        "core_p": "**Core Personality**: {}",
        "trajectory": "**Life Trajectory**: {}",
        "success_reasons": "**Cosmic Connections Hit:**\n\n{}",
        "warning": "The gears of fate turn in secret; no strong direct connections found yet...",
        "score": "Resonance Index: {} pts (For entertainment only)",
        "footer": "Note: This app is for fun. A historical figure's destiny is determined by their era and actions. This analysis offers another perspective for self-discovery.",
        
        # 匹配理由文案
        "reason_zodiac": "**[Zodiac Resonance]**: Both of you are born in the year of {}, indicating similar underlying life cycles and rhythm in Eastern astrology.",
        "reason_sign": "**[Astrological Overlap]**: Both are {}. Ruled by the same celestial body, you share strong commonalities in emotional expression and subconsciousness.",
        "reason_element": "**[Elemental Harmony]**: Both belong to {} signs ({} and {}), meaning your fundamental elements of perceiving the world are aligned.",
        "reason_wuxing": "**[Five Elements Sync]**: Both share the {} element, suggesting you have identical attributes in the flow of life energy and action style.",
        "reason_tiangan": "**[Heavenly Stem Match]**: Both share the {} stem. In ancient calendars, this means you possess similar initial drives and personality foundations.",
        "reason_hex": "**[Hexagram Guidance]**: Your destinies point to the same hexagram, '{}', implying you may make similar choices at major life turning points.",
        "vibe_1": "**[Aura Entanglement]**: Combining the {} element energy and '{}' hexagram spacetime, your decision logic in specific scenarios is astonishingly similar.",
        "vibe_2": "**[Echo of Eras]**: Despite different eras, your astrological trajectories show a fascinating mirror image at the intersection of '{}' and the present.",
        "vibe_3": "**[Soul Alignment]**: Ancient texts say those with {} constitution often show resilience and open-mindedness similar to {} in mid-to-late life.",
        "vibe_4": "**[Magnetic Resonance]**: Your birth energy field ({} / {}) has a subtle quantum resonance with this figure's life map."
    }
}

# ================= 2. 基础算法与数据 =================
ZODIAC_CN = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
ZODIAC_EN = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
TIANGAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
WUXING_EN = {"木": "Wood", "火": "Fire", "土": "Earth", "金": "Metal", "水": "Water"}

def get_western_zodiac(month, day, lang):
    # 返回 (星座, 四象)
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return ("白羊座", "火象") if lang=="中文" else ("Aries", "Fire")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return ("金牛座", "土象") if lang=="中文" else ("Taurus", "Earth")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21): return ("双子座", "风象") if lang=="中文" else ("Gemini", "Air")
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22): return ("巨蟹座", "水象") if lang=="中文" else ("Cancer", "Water")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return ("狮子座", "火象") if lang=="中文" else ("Leo", "Fire")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return ("处女座", "土象") if lang=="中文" else ("Virgo", "Earth")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23): return ("天秤座", "风象") if lang=="中文" else ("Libra", "Air")
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22): return ("天蝎座", "水象") if lang=="中文" else ("Scorpio", "Water")
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21): return ("射手座", "火象") if lang=="中文" else ("Sagittarius", "Fire")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19): return ("摩羯座", "土象") if lang=="中文" else ("Capricorn", "Earth")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18): return ("水瓶座", "风象") if lang=="中文" else ("Aquarius", "Air")
    else: return ("双鱼座", "水象") if lang=="中文" else ("Pisces", "Water")

def get_ganzhi(year):
    stem = TIANGAN[(year - 4) % 10]
    wuxing_map = {"甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土", "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"}
    return stem, wuxing_map[stem]

def get_hexagram(month, day, lang):
    gua_cn = ["乾为天", "坤为地", "水雷屯", "山水蒙", "水天需", "天水讼", "地水师", "水地比", "风天小畜", "天泽履", "地天泰", "天地否", "天火同人", "火天大有", "地山谦", "雷地豫"]
    gua_en = ["The Creative", "The Receptive", "Difficulty at the Beginning", "Youthful Folly", "Waiting", "Conflict", "The Army", "Holding Together", "Small Taming", "Treading", "Peace", "Standstill", "Fellowship", "Great Possession", "Modesty", "Enthusiasm"]
    idx = (month * day) % len(gua_cn)
    return gua_cn[idx] if lang == "中文" else gua_en[idx]

# ================= 3. 历史人物库 =================
figures = [
    {
        "name_cn": "曹操", "name_en": "Cao Cao", "era_cn": "东汉末年", "era_en": "Late Eastern Han",
        "tiangan": "庚", "zodiac_cn": "鼠", "zodiac_en": "Rat", "sign_cn": "双子座", "sign_en": "Gemini", 
        "element_cn": "风象", "element_en": "Air", "wuxing": "金", "hex_cn": "乾为天", "hex_en": "The Creative",
        "achievement_cn": "统一北方，奠定曹魏基业，开创建安文学。", "achievement_en": "Unified Northern China, laid the foundation of Cao Wei, pioneered Jian'an literature.",
        "personality_cn": "雄才大略、多疑冷酷、唯才是举、极度务实。", "personality_en": "Ambitious, suspicious, meritocratic, extremely pragmatic.",
        "trajectory_cn": "从洛阳北部尉起家，经历讨董、迎汉献帝、官渡之战，最终成为挟天子以令诸侯的北方霸主。", "trajectory_en": "Rose from a local official to a northern warlord, surviving numerous battles to become the de facto ruler of the Han Dynasty."
    },
    {
        "name_cn": "达·芬奇", "name_en": "Da Vinci", "era_cn": "文艺复兴", "era_en": "Renaissance",
        "tiangan": "壬", "zodiac_cn": "羊", "zodiac_en": "Goat", "sign_cn": "金牛座", "sign_en": "Taurus", 
        "element_cn": "土象", "element_en": "Earth", "wuxing": "水", "hex_cn": "山水蒙", "hex_en": "Youthful Folly",
        "achievement_cn": "绘制《蒙娜丽莎》，留下大量解剖、机械手稿，被誉为最接近‘全知’的人。", "achievement_en": "Painted the Mona Lisa, left extensive anatomy and engineering manuscripts, known as the closest to an 'omniscient' person.",
        "personality_cn": "充满狂热的好奇心，追求完美，思维发散，极其理智。", "personality_en": "Fanatical curiosity, perfectionist, divergent thinker, highly rational.",
        "trajectory_cn": "在佛罗伦萨、米兰和法国之间辗转，受雇于各地贵族，不断探索艺术与科学的边界。", "trajectory_en": "Traveled between Florence, Milan, and France, employed by nobles, constantly exploring the boundaries of art and science."
    },
    {
        "name_cn": "武则天", "name_en": "Wu Zetian", "era_cn": "唐朝", "era_en": "Tang Dynasty",
        "tiangan": "戊", "zodiac_cn": "狗", "zodiac_en": "Dog", "sign_cn": "水瓶座", "sign_en": "Aquarius", 
        "element_cn": "风象", "element_en": "Air", "wuxing": "土", "hex_cn": "坤为地", "hex_en": "The Receptive",
        "achievement_cn": "建立武周，成为中国历史上唯一的正统女皇帝，承上启下开元盛世。", "achievement_en": "Founded the Wu Zhou dynasty, the only orthodox female emperor in Chinese history, bridging to the Kaiyuan era.",
        "personality_cn": "极具魄力、不择手段、高度自律、具有超前的战略眼光。", "personality_en": "Highly decisive, ruthless, self-disciplined, possessing visionary strategic thinking.",
        "trajectory_cn": "从唐太宗才人，到感业寺削发为尼，再到重返宫廷，最终废唐建周，晚年神龙政变后退位。", "trajectory_en": "From a Tang concubine to a nun, then returning to the palace to eventually establish her own dynasty, abdicating after a coup in her later years."
    },
    {
        "name_cn": "马斯克", "name_en": "Elon Musk", "era_cn": "当代", "era_en": "Contemporary",
        "tiangan": "辛", "zodiac_cn": "猪", "zodiac_en": "Pig", "sign_cn": "巨蟹座", "sign_en": "Cancer", 
        "element_cn": "水象", "element_en": "Water", "wuxing": "金", "hex_cn": "乾为天", "hex_en": "The Creative",
        "achievement_cn": "创立SpaceX、特斯拉，推动商业航天与电动汽车革命。", "achievement_en": "Founded SpaceX and Tesla, driving revolutions in commercial spaceflight and electric vehicles.",
        "personality_cn": "极度冒险、第一性原理思维、工作狂、挑战常规。", "personality_en": "Extreme risk-taker, first-principles thinker, workaholic, challenges the status quo.",
        "trajectory_cn": "从南非到北美，从PayPal到SpaceX/特斯拉，多次在破产边缘逆转，成为世界首富。", "trajectory_en": "From South Africa to North America, from PayPal to SpaceX/Tesla, reversing near-bankruptcy multiple times to become the world's richest person."
    }
]

# ================= 4. 推演匹配逻辑 =================
def calculate_similarity(user_stem, user_zodiac_cn, user_sign_cn, user_element_cn, user_wuxing, user_hex_cn, fig, lang, t):
    score = 0
    reasons = []
    
    # 统一转换为当前语言环境进行比对
    idx_zodiac = ZODIAC_CN.index(user_zodiac_cn)
    cur_zodiac = user_zodiac_cn if lang=="中文" else ZODIAC_EN[idx_zodiac]
    cur_sign, cur_element = get_western_zodiac(1, 1, lang) if False else (user_sign_cn if lang=="中文" else "Aries", user_element_cn if lang=="中文" else "Fire")
    cur_wuxing = user_wuxing if lang=="中文" else WUXING_EN[user_wuxing]
    cur_hex = user_hex_cn if lang=="中文" else "The Creative"

    if fig[f"zodiac_{'cn' if lang=='中文' else 'en'}"] == cur_zodiac:
        score += 3
        reasons.append(t["reason_zodiac"].format(cur_zodiac))
    
    if fig[f"sign_{'cn' if lang=='中文' else 'en'}"] == cur_sign:
        score += 3
        reasons.append(t["reason_sign"].format(cur_sign))
    elif fig[f"element_{'cn' if lang=='中文' else 'en'}"] == cur_element:
        score += 2
        reasons.append(t["reason_element"].format(cur_element, fig[f"sign_{'cn' if lang=='中文' else 'en'}"], cur_sign))
    
    if fig["wuxing"] == user_wuxing:
        score += 2
        reasons.append(t["reason_wuxing"].format(cur_wuxing))
    
    if fig["tiangan"] == user_stem:
        score += 2
        reasons.append(t["reason_tiangan"].format(fig["tiangan"]))

    if fig[f"hex_{'cn' if lang=='中文' else 'en'}"] == cur_hex:
        score += 4
        reasons.append(t["reason_hex"].format(cur_hex))

    # 补充玄学理由
    random.seed(fig["name_cn"] + user_zodiac_cn + str(score))
    vibe_reasons = [
        t["vibe_1"].format(cur_wuxing, cur_hex),
        t["vibe_2"].format(fig[f"era_{'cn' if lang=='中文' else 'en'}"]),
        t["vibe_3"].format(cur_element, fig[f"name_{'cn' if lang=='中文' else 'en'}"]),
        t["vibe_4"].format(cur_zodiac, cur_wuxing)
    ]
    
    while len(reasons) < 3:
        vibe = random.choice(vibe_reasons)
        if vibe not in reasons:
            reasons.append(vibe)
            score += random.randint(1, 2)

    return score, reasons

# ================= 5. 页面渲染 =================
st.set_page_config(page_title="Destiny Analyzer", page_icon="🌌")

# 在页面顶部放置语言选择按钮
lang = st.radio("", ["中文", "English"], horizontal=True, label_visibility="collapsed")
t = TEXTS[lang]

st.title(t["title"])
st.markdown(t["subtitle"])

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(t["birth_date"])
        sub_col1, sub_col2, sub_col3 = st.columns(3)
        current_year = date.today().year
        select_year = sub_col1.selectbox(t["year"], range(1920, current_year + 1), index=70, label_visibility="collapsed")
        select_month = sub_col2.selectbox(t["month"], range(1, 13), index=0, label_visibility="collapsed")
        select_day = sub_col3.selectbox(t["day"], range(1, 32), index=0, label_visibility="collapsed")
    with col2:
        address = st.text_input(t["address"], value=t["address_default"])
    
    submitted = st.form_submit_button(t["submit"])

if submitted:
    year, month, day = select_year, select_month, select_day
    
    # 计算基础属性
    user_zodiac_cn = ZODIAC_CN[(year - 4) % 12]
    user_sign_cn, user_element_cn = get_western_zodiac(month, day, "中文")
    user_stem, user_wuxing = get_ganzhi(year)
    user_hex_cn = get_hexagram(month, day, "中文")
    
    # 计算展示属性
    idx_zodiac = (year - 4) % 12
    user_zodiac_display = ZODIAC_CN[idx_zodiac] if lang=="中文" else ZODIAC_EN[idx_zodiac]
    user_sign_display, _ = get_western_zodiac(month, day, lang)
    user_wuxing_display = user_wuxing if lang=="中文" else WUXING_EN[user_wuxing]
    user_hex_display = user_hex_cn if lang=="中文" else get_hexagram(month, day, "English")
    
    st.markdown("---")
    st.subheader(t["profile_title"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(t["hexagram"], user_hex_display)
    c2.metric(t["ganzhi"], f"{user_stem}{user_zodiac_display}")
    c3.metric(t["sign"], user_sign_display)
    c4.metric(t["wuxing"], user_wuxing_display)
    
    st.caption(t["caption_calc"].format(address))
    
    # 匹配
    results = []
    for fig in figures:
        score, reasons = calculate_similarity(user_stem, user_zodiac_cn, user_sign_cn, user_element_cn, user_wuxing, user_hex_cn, fig, lang, t)
        results.append((score, fig, reasons))
    
    results.sort(reverse=True, key=lambda x: x[0])
    top3 = results[:3]
    
    st.markdown("---")
    st.subheader(t["match_title"])
    
    for i, (score, fig, reasons) in enumerate(top3, 1):
        with st.container():
            name_display = fig["name_cn"] if lang=="中文" else fig["name_en"]
            era_display = fig["era_cn"] if lang=="中文" else fig["era_en"]
            st.markdown(f"### {i}. {name_display} ({era_display})")
            
            st.markdown(t["achievement"].format(fig[f"achievement_{'cn' if lang=='中文' else 'en'}"]))
            
            # 磁场标签
            magnetic_text = t["magnetic"].format(
                f"{fig['tiangan']}{fig['zodiac_cn']}年" if lang=="中文" else f"{fig['tiangan']} {fig['zodiac_en']} Year",
                fig[f"sign_{'cn' if lang=='中文' else 'en'}"],
                fig['wuxing'] if lang=="中文" else WUXING_EN[fig['wuxing']],
                fig[f"hex_{'cn' if lang=='中文' else 'en'}"]
            )
            st.markdown(magnetic_text)
            
            with st.expander(t["expand_text"]):
                st.markdown(t["core_p"].format(fig[f"personality_{'cn' if lang=='中文' else 'en'}"]))
                st.markdown(t["trajectory"].format(fig[f"trajectory_{'cn' if lang=='中文' else 'en'}"]))
            
            if reasons:
                reason_text = "\n".join([f"- {r}" for r in reasons])
                st.success(t["success_reasons"].format(reason_text))
            else:
                st.warning(t["warning"])
                
            st.caption(t["score"].format(score))
            st.markdown("---")

st.caption(t["footer"])