import Bar from "./Bar";

export default function Header(props) {
    return (
        <Bar>

            <header className="flex items-center justify-between">
                <h1 className='text-4xl'>Expert Eight Ball</h1>
                <p>{props.count} questions answered</p>
            </header>
        </Bar>
    )
}
