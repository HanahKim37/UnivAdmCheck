import streamlit as st
import pandas as pd
from io import BytesIO

# 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드 하세요", type=['xlsx'])

if uploaded_file:
    # 엑셀 파일 읽기
    df = pd.read_excel(uploaded_file)
    st.write("업로드된 데이터", df.head())

    # 조회를 위해 활용할 데이터 추출
    # 이 부분은 실제 조회 기능에 따라 구현되어야 합니다

    # 결과를 생성하는 로직 (예시)
    # 실제 조회 기능을 구현하고 싶다면 대학의 합격자 조회 페이지에 대한 웹 스크래핑 로직이 필요
    results = df.copy()
    results['합격 여부'] = "조회 필요"  # 여기서 실제 조회 결과를 반영

    st.write("조회 결과", results)

    # 엑셀 파일로 다운로드
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data

    download_data = to_excel(results)
    st.download_button(label="결과 다운로드", data=download_data, file_name='result.xlsx')
