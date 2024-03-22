import { Input } from '@nextui-org/react';
import React from 'react';

export default function Login() {
  return (
    <div className="grid place-items-center">
      <div className="flex w-[90vw] flex-wrap justify-center gap-4">
        <Input className="w-1/3" type="email" label="Email" />
        <Input
          className="w-1/3"
          type="email"
          label="Email"
          placeholder="Enter your email"
        />
      </div>
    </div>
  );
}
