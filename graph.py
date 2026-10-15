import pandas as pd
import streamlit as st

# 1. 페이지 제목 및 설명 설정
st.title("📚 공부 습관 대시보드")
st.caption("학생들의 공부 시간, 스마트폰 사용 시간, 성적 데이터를 분석합니다.")

# 2. 데이터 불러오기 (study.csv)
# study.csv 파일은 이 파이썬 코드 파일과 같은 폴더에 있어야 합니다.
df = pd.read_csv("study.csv")

# 3. 주요 요약 지표 (st.metric) 계산
total_students = len(df)  # 전체 학생 수
avg_score = df["점수"].mean()  # 평균 점수
avg_study_time = df["공부시간"].mean()  # 평균 공부시간

# 요약 지표를 한 줄(3개의 컬럼)에 나란히 배치
col1, col2, col3 = st.columns(3)
col1.metric("총 학생 수", f"{total_students}명")
col2.metric("평균 점수", f"{avg_score:.1f}점")
col3.metric("평균 공부시간", f"{avg_study_time:.1f}시간")

st.divider()  # 구분선 추가

# 4. 필터링을 위한 슬라이더 설정 (st.slider)
# 공부시간의 최소/최대값을 기준으로 슬라이더 범위를 지정합니다.
min_time_val = float(df["공부시간"].min())
max_time_val = float(df["공부시간"].max())

selected_min_time = st.slider(
    "최소 공부시간을 선택하세요 (시간 단위)",
    min_value=min_time_val,
    max_value=max_time_val,
    value=min_time_val,  # 기본 선택값
    step=0.5,
)

# 5. 선택한 공부시간 이상인 학생 데이터만 필터링
filtered_df = df[df["공부시간"] >= selected_min_time]

st.subheader(f"🔍 필터링 결과 (공부시간 {selected_min_time}시간 이상: {len(filtered_df)}명)")

# 6. Streamlit 기본 차트 그리기

# (1) 공부시간 vs 점수 산점도 (Scatter Chart)
st.write("### 📈 공부시간과 점수의 관계 (산점도)")
st.scatter_chart(data=filtered_df, x="공부시간", y="점수")

# (2) 학생별 점수 막대 그래프 (Bar Chart)
st.write("### 📊 학생별 점수 비교 (막대 그래프)")
st.bar_chart(data=filtered_df, x="학생ID", y="점수")

# 7. 필터링된 데이터 테이블 보여주기 (참고용)
with st.expander("📄 상세 데이터 보기"):
    st.dataframe(filtered_df)