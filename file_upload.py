import streamlit as st

st.title("파/일/업/로/드")

upload_file = st.file_uploader("업로드할 파일을 선택하세요.")

if upload_file is not None:
    # 파일 이름 가져오기
    file_name = upload_file.name

    # 파일 저장 경로 설정 (현재 디렉토리에 저장)
    save_path = f"./{file_name}"

    # 업로드된 파일을 저장
    with open(save_path, "wb") as f:
        f.write(upload_file.getbuffer())

    st.write(f"업로드가 완료되었습니다! 파일이 `{save_path}`에 저장되었습니다.")