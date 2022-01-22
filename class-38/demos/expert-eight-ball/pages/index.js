import Head from 'next/head';
import EightBall from '../components/EightBall';
import Footer from '../components/Footer';
import Header from '../components/Header';
import QuestionForm from '../components/QuestionForm';
import Report from '../components/Report';
import { replies } from '../data';
import { useState } from 'react';




export default function Home() {

    const [answeredQuestions, setAnsweredQuestions] = useState([]);

    function handleQuestionAsked(question) {
        // need to answer the question
        const randIndex = Math.floor(Math.random() * replies.length);
        const reply = replies[randIndex];
        const answeredQuestion = {
            question: question,
            answer: reply,
            id: answeredQuestions.length
        }
        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);

    }

    function getAnswer() {
        if (answeredQuestions.length == 0) {
            return "Waiting...";
        } else {
            return answeredQuestions[answeredQuestions.length - 1].answer;
        }
    }

    return (
        <div>

            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <Header count={answeredQuestions.length} />
            <QuestionForm onQuestionAsked={handleQuestionAsked} />
            <EightBall answer={getAnswer()} />
            <Report questions={answeredQuestions} />
            <Footer />

        </div>
    )
}
