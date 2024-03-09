import { Input } from "@nextui-org/react";

export default function Login() {
  return (
    <div className="">
      <div className="flex w-full h-screen flex-wrap md:flex-nowrap gap-4">
        <Input type="email" label="Email" />
        <Input type="email" label="Email" placeholder="Enter your email" />
      </div>
    </div>
  );
}
