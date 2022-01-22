import Link from 'next/link'
import Bar from './Bar'

export default function Footer() {
    return (
        <Bar>
            <footer>
                <Link href="/careers">
                    <a className="px-4 py-2 bg-gray-700 rounded-lg">Careers</a>
                </Link>
            </footer>
        </Bar>
    )
}
