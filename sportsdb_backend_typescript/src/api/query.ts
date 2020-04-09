import { DocumentNode } from 'graphql';
import { gql } from 'apollo-server';
import fs from "fs";
import path from "path";

import { PrismaClient } from '@prisma/client'
import { Datasource } from '@prisma/client/runtime';
const prisma = new PrismaClient()

var datastore_host = process.env.DATASTORE_HOST ? process.env.DATASTORE_HOST : 'localhost'
process.env.DATABASE_URL=`postgresql://postgres:1234@${datastore_host}/sportsdb`

export class Query {

    constructor() {

    }

    typedefs(): DocumentNode {
        var schema = fs.readFileSync(path.join(__dirname, "../../schema/query.graphql"), "utf8")
        return gql`${schema}`
    }

    resolvers(): any {
        return {
            Query: {
                players: resolve_players
            }
        };
    }
}

var resolve_players = async (parent: any, args: any, context: any, info: any) => {
    return await prisma.display_names.findMany({where: { entity_type: 'persons' }, first: 20})
}
