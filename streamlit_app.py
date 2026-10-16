import streamlit as st

st.set_page_config(
    page_title='임하연 | 나를 소개합니다',
    page_icon='💙',
    layout='wide',
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

    :root {
        --ink: #17375e;
        --blue: #3979bd;
        --sky: #e9f6ff;
        --line: #d8eafb;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse at 8% 10%, rgba(255,255,255,.92), transparent 35%),
            linear-gradient(135deg, #e4f4ff 0%, #cce8ff 48%, #e6f5ff 100%);
        color: var(--ink);
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 960px; padding-top: 3rem; }
    [data-testid="stMarkdownContainer"] { color: var(--ink); }

    .hero {
        position: relative;
        overflow: hidden;
        padding: clamp(2rem, 6vw, 4.5rem);
        border: 1px solid rgba(255,255,255,.8);
        border-radius: 28px;
        background: linear-gradient(125deg, rgba(255,255,255,.94), rgba(239,249,255,.84));
        box-shadow: 0 20px 55px rgba(70, 133, 188, .14);
    }

    .hero::after {
        content: "";
        position: absolute;
        right: -90px;
        bottom: -145px;
        width: 340px;
        height: 260px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(166,218,255,.55), rgba(221,242,255,.18));
        transform: rotate(-18deg);
    }

    .eyebrow {
        margin: 0 0 1rem;
        color: #4d88bd;
        font-family: 'Jua', sans-serif;
        font-size: 1rem;
    }

    .hero h1 {
        position: relative;
        z-index: 1;
        margin: 0;
        color: var(--ink);
        font-family: 'Jua', sans-serif;
        font-size: clamp(2.7rem, 7vw, 4.7rem);
        line-height: 1.12;
    }

    .hero .intro {
        position: relative;
        z-index: 1;
        max-width: 590px;
        margin: 1.3rem 0 0;
        color: #52708e;
        font-size: 1.12rem;
        line-height: 1.9;
    }

    .hero .hello {
        position: relative;
        z-index: 1;
        display: inline-block;
        margin-top: 1.5rem;
        padding: .65rem 1rem;
        border-radius: 999px;
        background: #e4f3ff;
        color: #3979bd;
        font-family: 'Jua', sans-serif;
    }

    .section-title {
        margin: 2.5rem 0 1rem;
        color: var(--ink);
        font-family: 'Jua', sans-serif;
        font-size: 1.65rem;
    }

    .profile-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
    }

    .info-card {
        min-height: 145px;
        padding: 1.25rem;
        border: 1px solid rgba(255,255,255,.92);
        border-radius: 18px;
        background: rgba(255,255,255,.76);
        box-shadow: 0 8px 24px rgba(69, 130, 183, .08);
    }

    .info-card .icon { font-size: 1.55rem; }
    .info-card .label { margin: .65rem 0 .3rem; color: #7290aa; font-size: .83rem; }
    .info-card .value { margin: 0; color: var(--ink); font-family: 'Jua', sans-serif; font-size: 1.12rem; }

    .story {
        padding: 1.5rem 1.7rem;
        border-left: 4px solid #86c4f4;
        border-radius: 0 16px 16px 0;
        background: rgba(255,255,255,.58);
        color: #52708e;
        line-height: 1.9;
    }

    .story strong { color: var(--ink); }

    .footer {
        margin: 2.8rem 0 1rem;
        color: #6d8ba7;
        text-align: center;
        font-size: .92rem;
    }

    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] { padding: 1.5rem 1rem 2rem; }
        .hero { border-radius: 22px; }
        .profile-grid { grid-template-columns: 1fr; }
        .info-card { min-height: auto; }
    }
    </style>

    <main>
      <section class="hero">
        <p class="eyebrow">MY LITTLE PROFILE · 2026</p>
        <h1>안녕하세요,<br>임하연입니다! 💙</h1>
        <p class="intro">배우고 싶은 것도, 만들어 보고 싶은 것도 많은<br>경복비즈니스고등학교 IT과 3학년 임하연입니다.</p>
        <span class="hello">반가워요! (｡•̀ᴗ-)✧</span>
      </section>

      <h2 class="section-title">하연이를 소개해요 <span>🫧</span></h2>
      <section class="profile-grid">
        <article class="info-card">
          <div class="icon">🏫</div>
          <p class="label">학교</p>
          <p class="value">경복비즈니스고등학교</p>
        </article>
        <article class="info-card">
          <div class="icon">💻</div>
          <p class="label">학년 · 전공</p>
          <p class="value">3학년 · IT과</p>
        </article>
        <article class="info-card">
          <div class="icon">🚲</div>
          <p class="label">요즘 좋아하는 것</p>
          <p class="value">자전거 타기</p>
        </article>
      </section>

      <h2 class="section-title">좋아하는 순간 🚴‍♀️</h2>
      <div class="story">
        자전거를 타고 바람을 느끼며 달리는 시간이 좋아요.<br>
        새로운 길을 발견하듯, IT 분야에서도 하나씩 배우며<br>
        저만의 가능성을 넓혀 가고 싶어요. <strong>슝슝! (๑˃̵ᴗ˂̵)و</strong>
      </div>

      <h2 class="section-title">앞으로의 목표 ✨</h2>
      <div class="story">
        학교에서 배운 IT 지식을 바탕으로 계속 성장해서<br>
        <strong>IT 분야 기업에 취업하는 것</strong>이 제 진로 목표예요.<br>
        차근차근 경험을 쌓아 믿고 함께 일할 수 있는 사람이 되고 싶습니다. 🌱
      </div>

      <p class="footer">오늘도 한 걸음씩, 나답게 성장 중 💙 ( ˶ˆᗜˆ˵ )</p>
    </main>
    """,
    unsafe_allow_html=True,
)
