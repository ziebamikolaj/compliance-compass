import {
  Button,
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from '@nextui-org/react';
import Link from 'next/link';
import React from 'react';

const Navigation = () => (
  <Navbar>
    <NavbarBrand>
      <Link className="font-bold text-inherit" href="/">
        Compliance Compass
      </Link>
    </NavbarBrand>
    <NavbarContent className="hidden gap-4 sm:flex" justify="center">
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

export default Navigation;
