"use client";

import { signIn, signOut, useSession } from "next-auth/react";
export default function HomePage() {
  const { data: sessionData } = useSession();

  return (
    <div className='flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white'>
      <div className='container flex flex-col items-center justify-center gap-12 px-4 py-16'>
        <h1 className='text-5xl font-extrabold tracking-tight sm:text-[5rem]'>
          Create <span className='text-[hsl(280,100%,70%)]'>T3</span> App
        </h1>
        <div className='flex flex-col items-center gap-2'>
          <p className='text-2xl text-white'>Ready to build!</p>
          <div className='flex flex-col items-center justify-center gap-4'>
            <p className='text-center text-2xl text-white'>
              {sessionData && (
                <span>Logged in as {sessionData.user?.name}</span>
              )}
            </p>
            <button
              className='rounded-full bg-white/10 px-10 py-3 font-semibold text-white no-underline transition hover:bg-white/20'
              onClick={sessionData ? () => signOut() : () => signIn()}
            >
              {sessionData ? "Sign out" : "Sign in"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
