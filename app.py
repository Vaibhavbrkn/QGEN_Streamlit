from quiz.question import Question
import streamlit as st


@st.cache
def load(message, mc, fi):
    q = Question("s2v_old")
    return q.generate(message,  min_mcq_question=1, max_mcq_question=mc, min_fill_ques=1, max_fill_ques=fi)


def main():
    st.title("Question Generation with NLP")
    message = st.text_area("Enter Text", "Type Here ..")
    mc = st.slider('Number of MCQ Question', 1, 7, 1)
    fi = st.slider('Number of Fill In Blank Question', 1, 4, 1)

    if st.button('Generate'):
        ans = load(message, mc, fi)
        st.write("MCQ Questions")
        for i in range(len(ans['mcq'])):
            container = st.container()
            container.write("{}. {}".format(i+1, ans['mcq'][i]['question']))
            col1, col2 = container.columns(2)
            with col1:
                st.button(ans['mcq'][i]['choice'][0], key=(i+1)*10 + 1)
            with col2:
                st.button(ans['mcq'][i]['choice'][1], key=(i+1)*10 + 2)

            col1, col2 = container.columns(2)
            with col1:
                st.button(ans['mcq'][i]['choice'][2], key=(i+1)*10 + 3)
            with col2:
                st.button(ans['mcq'][i]['choice'][3], key=(i+1)*10 + 4)

        container.write("Fill In Blank Questions")
        for i in range(len(ans['fill'])):
            container.write("{}. {}".format(i+1, ans['fill'][i]['question']))

        with st.expander("Show Answer"):
            container = st.container()
            container.write('MCQ answer :')
            for i in range(len(ans['mcq'])):
                container.write("{}. {}".format(i+1, ans['mcq'][i]['answer']))

            container.write("")

            container.write('Fill In Blank answer :')
            for i in range(len(ans['fill'])):
                container.write("{}. {}".format(i+1, ans['fill'][i]['answer']))


if __name__ == '__main__':
    main()
