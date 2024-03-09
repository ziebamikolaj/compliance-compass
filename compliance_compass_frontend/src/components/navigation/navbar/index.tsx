import {
  Button,
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from "@nextui-org/react";
import Link from "next/link";

const Navigation = () => {
  return (
    <Navbar>
      <NavbarBrand>
        <Link className="font-bold text-inherit" href="/">
          Compliance Compass
        </Link>
      </NavbarBrand>
      <NavbarContent className="hidden sm:flex gap-4" justify="center">
        <NavbarItem isActive>
          <Link aria-current="page" href="/about">
            About
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link href="/blog" color="foreground">
            Blog
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link color="foreground " href="/pricing">
            Pricing
          </Link>
        </NavbarItem>
      </NavbarContent>
      <NavbarContent justify="end">
        <NavbarItem className="hidden lg:flex">
          <Link href="/login">Login</Link>
        </NavbarItem>
        <NavbarItem>
          <Button as={Link} color="primary" href="/signup" variant="flat">
            Sign Up
          </Button>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
};

export default Navigation;
