export default function EightBall(props) {
    return (
        <div className="mx-auto bg-gray-900 rounded-full w-96 h-96">
            <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                <p className="text-2xl">{props.answer}</p>
            </div>
        </div>
    )
}
