import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 캐릭터 추천",
    page_icon="🎮",
    layout="centered"
)

st.title("🎮 MBTI 포켓몬 캐릭터 추천")
st.write("MBTI를 선택하면 나와 닮은 포켓몬 캐릭터와 성격을 알려줘요!")

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "personality": "조용하지만 강한 카리스마가 있어요. 깊이 생각하고 전략적으로 움직이는 타입이라, 목표가 생기면 끝까지 집중해서 해내요."
    },
    "INTP": {
        "pokemon": "메타몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
        "personality": "호기심이 많고 상상력이 풍부해요. 정해진 틀보다 새로운 방식으로 생각하는 걸 좋아하고, 다양한 가능성을 탐구해요."
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "personality": "자신감 있고 추진력이 강해요. 목표를 정하면 빠르게 움직이며, 사람들을 이끄는 리더십이 돋보여요."
    },
    "ENTP": {
        "pokemon": "고라파덕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png",
        "personality": "엉뚱하지만 아이디어가 넘쳐요. 새로운 도전을 좋아하고, 기발한 생각으로 주변을 놀라게 하는 매력이 있어요."
    },
    "INFJ": {
        "pokemon": "라티아스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/380.png",
        "personality": "섬세하고 따뜻한 마음을 가졌어요. 조용하지만 사람의 마음을 잘 이해하고, 의미 있는 목표를 위해 꾸준히 노력해요."
    },
    "INFP": {
        "pokemon": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "personality": "감수성이 풍부하고 가능성이 많은 타입이에요. 자신만의 가치관을 소중히 여기며 다양한 모습으로 성장할 수 있어요."
    },
    "ENFJ": {
        "pokemon": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "personality": "밝고 따뜻하며 사람들과 함께하는 것을 좋아해요. 주변 사람들에게 힘을 주고 긍정적인 에너지를 전해요."
    },
    "ENFP": {
        "pokemon": "파이리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        "personality": "열정적이고 호기심이 많아요. 새로운 경험을 좋아하고, 작은 일에도 신나게 반응하는 에너지가 있어요."
    },
    "ISTJ": {
        "pokemon": "꼬부기",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "personality": "성실하고 책임감이 강해요. 맡은 일을 차근차근 해내며, 약속을 잘 지키는 믿음직한 타입이에요."
    },
    "ISFJ": {
        "pokemon": "럭키",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
        "personality": "다정하고 배려심이 깊어요. 주변 사람을 잘 챙기고, 조용히 도움을 주는 따뜻한 매력이 있어요."
    },
    "ESTJ": {
        "pokemon": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "personality": "현실적이고 책임감이 강해요. 규칙과 질서를 중요하게 생각하며, 계획한 일을 정확하게 실행해요."
    },
    "ESFJ": {
        "pokemon": "푸린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "personality": "사교적이고 친근해요. 사람들과 어울리는 것을 좋아하고, 분위기를 부드럽고 즐겁게 만드는 능력이 있어요."
    },
    "ISTP": {
        "pokemon": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "personality": "침착하고 실용적인 문제 해결 능력이 뛰어나요. 말보다 행동으로 보여주며, 위기 상황에서도 차분해요."
    },
    "ISFP": {
        "pokemon": "님피아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/700.png",
        "personality": "감성적이고 섬세한 매력이 있어요. 자신만의 취향과 개성을 중요하게 생각하고 예술적인 표현을 좋아해요."
    },
    "ESTP": {
        "pokemon": "잠만보",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png",
        "personality": "느긋해 보이지만 현실 감각이 뛰어나요. 순간 판단력이 좋고 지금 이 순간을 즐기는 타입이에요."
    },
    "ESFP": {
        "pokemon": "토게피",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "personality": "밝고 사랑스러운 분위기를 가졌어요. 사람들에게 웃음을 주고 함께 있을 때 즐거운 에너지를 전해요."
    }
}

mbti_list = list(pokemon_data.keys())

mbti = st.selectbox(
    "👇 나의 MBTI를 선택하세요",
    mbti_list
)

result = pokemon_data[mbti]

st.divider()

st.subheader(f"✨ {mbti}와 닮은 포켓몬은?")

st.image(result["image"], width=250)

st.markdown(f"## {result['pokemon']}")
st.write(result["personality"])

st.divider()

st.info("※ 이 결과는 재미와 자기이해 활동을 위한 참고용입니다.")
