import Head from 'next/head'

export default function Home() {
    return (
        <div>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <body>

                <header className="bg-gray-500 text-gray-50 flex items-center justify-between p-4">
                    <h1 className="text-4xl">Expert 8 Ball</h1>
                    <p>1 questions answered</p>
                </header>

                <main>

                    <QuestionForm />

                    <EightBall />


                    <ResponseTable />





                </main>
                <footer className="bg-gray-500 mt-4 p-4 text-gray-50">
                    <nav>
                        <a href="">Careers</a>
                    </nav>
                </footer>
            </body>
        </div>
    )
}

function QuestionForm() {
    return (
        <form className="w-1/2 p-2 my-4 bg-gray-200 mx-auto flex">
            <input type="text" className="flex-auto pl-1" />
            <button className="px-2 bg-gray-500 text-gray-50">Ask</button>
        </form>
    )
}

function EightBall() {
    return (
        <div className="w-96 h-96 bg-gray-900 mx-auto my-4 rounded-full">
            <div className="w-48 h-48 rounded-full bg-gray-50 relative top-16 left-16 flex items-center justify-center">
                <p className="text-xl">Ask me anything</p>
            </div>
        </div>
    )
}

function ResponseTable() {
    return (
        <table className='w-1/2 mx-auto my-4'>
            <thead>
                <tr>
                    <th className="border border-gray-700">No.</th>
                    <th className="border border-gray-700">Question</th>
                    <th className="border border-gray-700">Response</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td className="pl-2 border border-gray-700">0</td>
                    <td className="pl-2 border border-gray-700">Is the darkside stronger?</td>
                    <td className="pl-2 border border-gray-700">Yes.</td>
                </tr>
            </tbody>

        </table>
    )
}
