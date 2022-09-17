import React from "react";
import { useEffect } from "react";

const AuthForm = function () {
    
    return (
      <div className="flex flex-1 w-full mx-auto justify-center">
        <form className="bg-black fill-gray-900 shadow-md rounded-md px-8 pt-6 pb-8 mb-4 my-44 ">
          <div className="mb-4">
            <input className="bg-black shadow appearance-none border-b-4 border-yellow-500 w-full py-2 text-white leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username"/>
          </div>
          <div className="mb-6">
            <input className="bg-black shadow appearance-none border-b-4 border-yellow-500 py-2 w-full text-white mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Password"/>
            <p className="text-red-500 text-xs italic">Please choose a password.</p>
          </div>
          <div className="flex items-center justify-between">
            <button className="bg-yellow-500 hover:bg-yellow-700 text-gray font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
              Sign In
            </button>
            <a className="px-3 text-gray-500 hover:text-white" href="">Forgot your password?</a>
          </div>
        </form>
      </div>
    );
  }
  
  export default AuthForm;
  