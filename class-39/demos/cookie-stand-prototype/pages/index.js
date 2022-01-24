import Head from 'next/head';
import Link from 'next/link';
import { useAuth } from '../contexts/auth';
import useResource from '../hooks/useResource';

export default function Home() {

    const { user, login, logout } = useAuth();

    return (
        <div className="p-4">
            <Head>
                <title>Cookie Stand Admin</title>
            </Head>
            {user ?
                <CookieStandAdmin user={user} logout={logout} />
                :
                <LoginForm onLogin={login} />
            }

        </div>
    );
}

function CookieStandAdmin({ user, logout }) {

    const { resources, deleteResource } = useResource();

    const standsCount = resources ? resources.length : 0;

    return (
        <>
            <CookieStandHeader user={user} logout={logout} />
            <CookieStandForm />
            <CookieStandTable stands={resources || []} deleteStand={deleteResource} />
            <CookieStandFooter standsCount={standsCount} />
        </>
    );
}

function CookieStandFooter({ standsCount }) {
    return <h2>{standsCount} Locations</h2>
}

function CookieStandHeader({ user, logout }) {
    return (
        <nav>
            <h2>{user.username}:{user.id}</h2>
            <button onClick={logout}>Log Out</button>
            <Link href="/overview">
                <a>Overview</a>
            </Link>
        </nav>
    );
}

function CookieStandForm() {

    const { user } = useAuth();
    const { createResource } = useResource();

    function handleSubmit(event) {
        event.preventDefault();
        const info = {
            location: event.target.location.value,
            minimum_customers_per_hour: parseInt(event.target.minimum.value),
            maximum_customers_per_hour: parseInt(event.target.maximum.value),
            average_cookies_per_sale: parseFloat(event.target.average.value),
            owner: user.id,
        };
        createResource(info);

    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset>
                <legend>Create Cookie Stand</legend>
                <input placeholder='location' name='location' />
                <input placeholder='minimum' name='minimum' />
                <input placeholder='maximum' name='maximum' />
                <input placeholder='average' name='average' />
                <button>create</button>
            </fieldset>
        </form>
    );
}

function CookieStandTable({ stands, deleteStand }) {
    return (
        <table className="my-8">
            <thead>
                <tr>
                    <th>Location</th>
                    <th>6 am</th>
                    <th>7 am</th>
                    <th>8 am</th>
                    <th>9 am</th>
                    <th>10 am</th>
                    <th>11 am</th>
                    <th>12 pm</th>
                    <th>1 pm</th>
                    <th>2 pm</th>
                    <th>3 pm</th>
                    <th>4 pm</th>
                    <th>5 pm</th>
                    <th>6 pm</th>
                    <th>7 pm</th>
                    <th>totals</th>
                </tr>
            </thead>
            <tbody>
                {stands.map(stand => (
                    <CookieStandRow key={stand.id} info={stand} deleteStand={deleteStand} />
                ))}
            </tbody>
        </table>
    );
}

function CookieStandRow({ info, deleteStand }) {

    function clickHandler() {
        deleteStand(info.id);
    }

    if (info.hourly_sales.length == 0) {
        // bunk data
        info.hourly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    }

    return (
        <tr>
            <td>{info.location} <button onClick={clickHandler}><svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
            </svg></button></td>
            {info.hourly_sales.map((slot, index) => <td key={index}>{slot}</td>)}
            <td>{info.hourly_sales.reduce((num, sum) => num + sum, 0)}</td>
        </tr>
    );
}


function LoginForm({ onLogin }) {

    async function handleSubmit(event) {
        event.preventDefault();
        onLogin(event.target.username.value, event.target.password.value);
    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset autoComplete='off'>
                <legend>Log In</legend>
                <label htmlFor="username">Username</label>
                <input name="username" />
                <label htmlFor="password">Password</label>
                <input type="password" name="password" />
                <button>Log In</button>
            </fieldset>
        </form>
    );
}
