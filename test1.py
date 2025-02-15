import sys
import os
import streamlit as st
# 서브모듈 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'excel'))

# 저장소 excel에서 함수 임포트 (모듈 파일명 "module_test.py", 함수명 "submodule_function")
from module_test import submodule_function

# 함수 사용 예
result = submodule_function()
st.write(result)

# 이 파일은 저장소 "test" 에 업로드함