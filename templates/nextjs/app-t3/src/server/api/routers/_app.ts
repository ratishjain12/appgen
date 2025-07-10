import { createTRPCRouter } from "~/server/api/root";
import { exampleRouter } from "~/server/api/routers/example";

export const appRouter = createTRPCRouter({
  example: exampleRouter,
});

export type AppRouter = typeof appRouter;
