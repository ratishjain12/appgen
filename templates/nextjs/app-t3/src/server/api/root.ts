import { initTRPC } from "@trpc/server";
import superjson from "superjson";

import { type Context } from "~/server/api/trpc";

const t = initTRPC.context<Context>().create({
  transformer: superjson,
  errorFormatter({ shape }) {
    return shape;
  },
});

export const createTRPCRouter = t.router;
export const publicProcedure = t.procedure;
